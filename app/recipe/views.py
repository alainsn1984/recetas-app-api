"""
Views for recipe APis
"""
from rest_framework import viewsets # noqa
from rest_framework.authentication import TokenAuthentication # noqa
from rest_framework.permissions import IsAuthenticated # noqa
from recipe import serializers  # noqa

from core.models import Recipe # noqa

class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs"""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all().order_by('-id')
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user)
