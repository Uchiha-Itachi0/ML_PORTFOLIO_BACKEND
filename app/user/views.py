"""
Views for the user API

"""

from rest_framework import generics
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from user.serializers import UserSerializers, LoginSerializer, TokenValidationSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken
from rest_framework_simplejwt.views import TokenObtainPairView



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class CreateUserView(generics.CreateAPIView):
    """Create the new user in the system"""
    serializer_class = UserSerializers


class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                tokens = get_tokens_for_user(user)
                return Response(tokens, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenValidationView(generics.GenericAPIView):
    serializer_class = TokenValidationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            UntypedToken(serializer.validated_data['token'])
            return Response(
                {
                    "status": True,
                    "message": "Token is valid"
                },
                status=status.HTTP_200_OK
            )
        except (InvalidToken, TokenError, serializers.ValidationError):
            return Response(
                {
                    "status": False,
                    "message": "Token is invalid or expired"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
