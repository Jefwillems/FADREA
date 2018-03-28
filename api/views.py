from rest_framework import permissions
from rest_framework import viewsets

from api.serializers import ProfileSerializer, HighscoreSerializer
from main.models import HighScores
from usermanagement.models import Profile


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
