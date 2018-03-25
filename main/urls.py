from django.conf.urls import url
from main.views import IndexView, GameView

urlpatterns = [
    url(r'^fish/$', GameView.as_view(), name='game'),
    url(r'^$', IndexView.as_view(), name='index'),
]
