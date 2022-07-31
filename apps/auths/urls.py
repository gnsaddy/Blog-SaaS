from django.urls import path, include
from rest_framework import routers

from .views import ping_pong, CookieTokenObtainPairView, CookieTokenRefreshView, FacultyUserViewSet

router = routers.DefaultRouter()
router.register(r'faculty', FacultyUserViewSet)


urlpatterns = [
    path('ping/', ping_pong),
    path('login/', CookieTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('relogin/',
         CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls))
]
