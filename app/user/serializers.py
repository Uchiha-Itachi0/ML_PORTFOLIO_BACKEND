"""
Serializers for User API
"""

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import UntypedToken


class UserSerializers(serializers.ModelSerializer):
    """Serializer for User Object"""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False)


class TokenValidationSerializer(serializers.Serializer):
    token = serializers.CharField()

    @staticmethod
    def validate_token(value):
        try:
            UntypedToken(value)
        except (InvalidToken, TokenError):
            raise serializers.ValidationError("Token is invalid or expired")
        return value
