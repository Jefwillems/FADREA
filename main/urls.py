from django.conf.urls import url
from main.views import IndexView, GameView, HighscoreView

urlpatterns = [
    url(r'^fish/$', GameView.as_view(), name='game'),
    url(r'^highscore/$', HighscoreView.as_view(), name='highscore'),
    url(r'^$', IndexView.as_view(), name='index'),
]
