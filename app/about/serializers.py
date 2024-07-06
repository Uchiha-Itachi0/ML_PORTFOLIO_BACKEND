from rest_framework import serializers
from core.models import About


class AboutSerializer(serializers.ModelSerializer):
    """Serializer for the About object"""

    skills = serializers.ListField(child=serializers.CharField(), default=list)
    color_text = serializers.ListField(child=serializers.CharField(), default=list)
    colors = serializers.ListField(child=serializers.CharField(), default=list)

    class Meta:
        model = About
        fields = ['content', 'skills', 'color_text', 'colors']

    def validate_content(self, value):
        if not isinstance(value, str) or not value.strip():
            raise serializers.ValidationError('Content must be a non-empty string.')
        return value

    def validate_skills(self, value):
        if not isinstance(value, list) or not value:
            raise serializers.ValidationError('Skills must be a non-empty list.')
        return value

    def validate_color_text(self, value):
        if not isinstance(value, list) or not value:
            raise serializers.ValidationError('Color text must be a non-empty list.')
        return value

    def validate_colors(self, value):
        if not isinstance(value, list) or not value:
            raise serializers.ValidationError('Colors must be a non-empty list.')
        return value
