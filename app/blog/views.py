""" View for the Blog API """

from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from core.models import Blogs
from blog.serializers import BlogSerializer


class GetAndCreateAPIView(generics.ListCreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return super().get_permissions()


class UpdateAndDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
