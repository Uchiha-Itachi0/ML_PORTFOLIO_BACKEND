""" View for the Blog API """

from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from core.models import Blogs
from blog.serializers import BlogSerializer


class PublicBlogView(generics.ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer


class AdminBlogCreateView(generics.CreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class AdminBlogUpdateView(generics.UpdateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class AdminBlogDeleteView(generics.DestroyAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
