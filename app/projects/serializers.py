"""Serializer for the Project API"""

from rest_framework import serializers
from core.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for the Project"""

    tags = serializers.ListField(child=serializers.CharField(), default=list)

    class Meta:
        model = Project
        fields = ['id', 'tags', 'time', 'title', 'subtitle', 'link']

    @staticmethod
    def validate_tags(value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Tags must be provided as a list")
        return value

    @staticmethod
    def validate_title(value):
        if not isinstance(value, str) or not value.strip():
            raise serializers.ValidationError('Title must be a non-empty string.')
        return value

    @staticmethod
    def validate_subtitle(value):
        if not isinstance(value, str) or not value.strip():
            raise serializers.ValidationError('Subtitle must be a non-empty string.')
        return value

    @staticmethod
    def validate_time(value):
        if not value:
            raise serializers.ValidationError('Published date must be provided.')
        return value
