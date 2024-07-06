from rest_framework import generics, permissions, status
from core.models import About
from about.serializers import AboutSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotFound
from django.utils.translation import gettext_lazy as _


class AboutRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = About.objects.first()
        if not obj:
            raise NotFound(_("About object not found."))
        return obj

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return super().get_permissions()

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as exc:
            return self.handle_exception(exc)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as exc:
            return self.handle_exception(exc)
