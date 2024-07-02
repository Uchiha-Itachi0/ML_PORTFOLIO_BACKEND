"""View for the About API"""

from rest_framework import generics, permissions
from core.models import About
from about.serializers import AboutSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class AboutView(generics.RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get_object(self):
        return About.objects.first()


class AboutUpdateView(generics.UpdateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return About.objects.first()
