from rest_framework import serializers
from core.models import Blogs


class BlogSerializer(serializers.ModelSerializer):
    """Serializer for the Blog object"""

    class Meta:
        model = Blogs
        fields = ['id', 'title', 'subtitle', 'time', 'link']

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
