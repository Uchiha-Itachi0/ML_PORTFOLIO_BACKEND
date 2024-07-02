""" Serializer for the Blog API """

from rest_framework import serializers
from core.models import Blogs


class BlogSerializer(serializers.ModelSerializer):
    """Serializer for the Blog API"""

    class Meta:
        model = Blogs
        fields = ['id', 'time', 'title', 'subtitle', 'link']
