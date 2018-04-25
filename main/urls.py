from django.conf.urls import url
from main.views import IndexView, GameView, HighscoreView, ArticleListView, ArticleView, ArtistListView, \
    ArtistDetailView, test

urlpatterns = [
    url(r'^fish/$', GameView.as_view(), name='game'),
    url(r'^test/$', test, name='test'),
    url(r'^highscore/$', HighscoreView.as_view(), name='highscore'),
    url(r'^news/$', ArticleListView.as_view(), name='news'),
    url(r'^news/(?P<slug>[-\w]+)/$', ArticleView.as_view(), name='article-detail'),
    url(r'^artists/$', ArtistListView.as_view(), name='artists'),
    url(r'^artists/(?P<slug>[-\w]+)/$', ArtistDetailView.as_view(), name="artist-detail"),
    url(r'^$', IndexView.as_view(), name='index'),

]
