from .models import CustomUser, FacultyUserModel
from rest_framework import serializers
from django.contrib.auth import password_validation
from rest_framework.decorators import authentication_classes, permission_classes


class FacultyUserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        validated_data['faculty'] = True
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    def first_name(self, instance):
        if instance.first_name is not None:
            return instance.first_name

    def last_name(self, instance):
        if instance.last_name is not None:
            return instance.last_name

    def expertise(self, instance):
        if instance.expertise is not None:
            return instance.expertise

    # set is_faculty to True
    def faculty(self, instance):
        return True

    class Meta:
        model = FacultyUserModel
        fields = ('id', 'sid', 'first_name', 'last_name', 'email', 'mobile', 'faculty', 'active',
                  'designation', 'expertise', 'experience', 'password', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
        extra_kwargs = {
            'password': {'write_only': True},
        }
