"""Serializer for the Project API"""

from rest_framework import serializers
from core.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for the Project"""

    tags = serializers.ListField(child=serializers.CharField(), default=list)

    class Meta:
        model = Project
        fields = ['id', 'tags', 'time', 'title', 'subtitle', 'link']

    def validate_tags(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Tags must be provided as a list")
        return value

