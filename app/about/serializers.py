# about/serializers.py
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

    def validate_skills(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError('Skills must be given as a list')
        return value

    def validate_color_text(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError('Color text must be given as a list')
        return value

    def validate_colors(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError('Colors must be given as a list')
        return value
