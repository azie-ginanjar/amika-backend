from django.contrib.auth import get_user_model
from requests import request
from rest_framework import serializers
from rest_framework.exceptions import bad_request

from user.models import Role

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "password", "username", "email", "name", "role")

    def create(self, validated_data):
        if not hasattr(Role, validated_data['role']):
            raise bad_request(request, Exception, 'Invalid Role', code=400)
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "name", "role")