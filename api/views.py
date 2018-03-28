from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.renderers import BrowsableAPIRenderer

from usermanagement.models import Profile
from api.serializers import ProfileSerializer, HighscoreSerializer
from api.models import HighScores
from api.renderers import BrowsableAPIRendererWithoutForms


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class HighscoreViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to post their highscore from within the fish game.
    """
    permission_classes = (permissions.AllowAny,)
    queryset = HighScores.objects.all()
    serializer_class = HighscoreSerializer
