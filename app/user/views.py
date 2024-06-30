"""
Views for the user API
"""
from rest_framework import generics, authentication, permissions # noqa
from rest_framework.authtoken.views import ObtainAuthToken # noqa
from rest_framework.settings import api_settings # noqa
from user.serializers import ( # noqa
    UserSerializer, # noqa
    AuthTokenSerializer, # noqa
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user