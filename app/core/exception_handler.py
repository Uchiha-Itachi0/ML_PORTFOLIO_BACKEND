# core/exception_handler.py
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError, AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    response = drf_exception_handler(exc, context)

    if response is not None:
        return response

    if isinstance(exc, NotFound):
        return Response({'error': str(exc)}, status=status.HTTP_404_NOT_FOUND)
    elif isinstance(exc, PermissionDenied):
        return Response({'error': str(exc)}, status=status.HTTP_403_FORBIDDEN)
    elif isinstance(exc, ValidationError):
        return Response({'error': exc.detail}, status=status.HTTP_400_BAD_REQUEST)
    elif isinstance(exc, AuthenticationFailed):
        return Response({'error': str(exc)}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'error': str(exc)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
