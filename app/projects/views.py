"""View for the Prject API"""

from core.models import Project
from projects.serializers import ProjectSerializer

from rest_framework import permissions, generics
from rest_framework_simplejwt.authentication import JWTAuthentication


class GetAndCreateProjectAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return super().get_permissions()


class UpdateAndDeleteProjectAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
