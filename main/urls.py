from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^fish/$', views.GameView.as_view(), name='game'),
    url(r'^test/$', views.test, name='test'),
    url(r'^highscore/$', views.HighscoreView.as_view(), name='highscore'),

    url(r'^news/$', views.ArticleListView.as_view(), name='news'),
    url(r'^news/(?P<slug>[-\w]+)/$', views.ArticleView.as_view(), name='article-detail'),
    url(r'^artists/$', views.ArtistListView.as_view(), name='artists'),
    url(r'^artists/(?P<slug>[-\w]+)/$', views.ArtistDetailView.as_view(), name="artist-detail"),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
