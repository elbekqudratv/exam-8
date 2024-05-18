from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import PasswordResets

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class PasswordCodeCheck(serializers.Serializer):
    code = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class PasswordEmailCodeSend(serializers.Serializer):
    email = serializers.EmailField(required=True)
