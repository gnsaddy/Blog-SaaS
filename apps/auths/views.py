from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer, TokenObtainPairSerializer
from django.middleware import csrf
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from .models import CustomUser, FacultyUserModel
from .serializers import FacultyUserSerializer
from ..utils import set_server_cookie


def ping_pong(request):
    return JsonResponse({"message": "ping-pong"})


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['id'] = user.id
        token['username'] = user.first_name + ' ' + user.last_name
        token['email'] = user.email
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['id'] = self.user.id
        data['name'] = self.user.first_name + ' ' + self.user.last_name
        data['mobile'] = self.user.mobile
        data['email'] = self.user.email
        user_type = None
        if self.user.is_superuser:
            user_type = 'admin'
        elif self.user.is_staff:
            user_type = 'staff'
        elif self.user.is_faculty:
            user_type = 'faculty'
        data['user_type'] = user_type
        data['sid'] = self.user.sid

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None

    def validate(self, attrs):
        print('CookieTokenRefreshSerializer.validate',
              self.context['request'].COOKIES.get('refresh_token'), flush=True)
        attrs['refresh'] = self.context['request'].COOKIES.get('refresh_token')
        if attrs['refresh']:
            return super().validate(attrs)
        else:
            raise InvalidToken(
                'No valid token found in cookie \'refresh_token\'')


class CookieTokenObtainPairView(TokenObtainPairView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            cookie_max_age = 3600 * 24 * 14  # 14 days
            # access token cookie
            set_server_cookie(response, 'access_token', response.data['access'], max_age=cookie_max_age)
            # refresh token cookie
            set_server_cookie(response, 'refresh_token', response.data['refresh'], max_age=cookie_max_age)

            # del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)

    serializer_class = MyTokenObtainPairSerializer


class CookieTokenRefreshView(TokenRefreshView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            cookie_max_age = 3600 * 24 * 14  # 14 days
            response.set_cookie(
                'refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=True, samesite='none',
                secure=False)

            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)

    serializer_class = CookieTokenRefreshSerializer


# FacultyUserViewSet
class FacultyUserViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = FacultyUserSerializer
    queryset = FacultyUserModel.objects.all()

    # list all users
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    # add new user
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return JsonResponse(serializer.data, status=201, headers=headers)
