"""Serializer for the about API"""

from rest_framework import serializers
from core.models import About


class AboutSerializer(serializers.ModelSerializer):
    """Serializer for the About object"""

    class Meta:
        model = About
        fields = ['content', 'skills', 'color_text', 'colors']
