from django.conf.urls import url
from main.views import IndexView, GameView, HighscoreView, test

urlpatterns = [
    url(r'^fish/$', GameView.as_view(), name='game'),
    url(r'^test/$', test, name='test'),
    url(r'^highscore/$', HighscoreView.as_view(), name='highscore'),
    url(r'^$', IndexView.as_view(), name='index'),

]
