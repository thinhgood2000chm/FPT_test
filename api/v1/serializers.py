from rest_framework import serializers

from api.base.serializer import InheritedSerializer


class LoginSerializerRequest(InheritedSerializer):
    username = serializers.CharField(help_text="username for login", required=True)
    password = serializers.CharField(help_text="password for login", required=True)


class LoginSerializerResponse(InheritedSerializer):
    token = serializers.CharField(help_text="token when login success", required=True)


class UserInfoSerializerResponse(InheritedSerializer):
    id = serializers.IntegerField(help_text="id of user", required=True)
    username = serializers.CharField(help_text="username of user", required=True)
    full_name = serializers.CharField(help_text="full name of user", required=True)


class RegisterSerializerRequest(InheritedSerializer):
    full_name = serializers.CharField(help_text="full name of user", required=True)
    username = serializers.CharField(help_text="username for login", required=True)
    password = serializers.CharField(help_text="password for login", required=True)