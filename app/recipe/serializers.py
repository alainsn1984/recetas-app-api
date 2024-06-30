"""
Serializer for recipe APIs
"""
from rest_framework import serializers # noqa

from core.models import Recipe # noqa

class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""
    class Meta:
        model = Recipe
        fields = ['title', 'time_minutes', 'price']
        read_only_fields = ['id']