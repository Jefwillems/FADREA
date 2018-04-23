from django.db.models import Max
from django.shortcuts import render_to_response
from django.views import generic

from main.models import HighScores, Article


class IndexView(generic.TemplateView):
    template_name = 'main/index.html'


class GameView(generic.TemplateView):
    template_name = 'main/game.html'


class ArticleListView(generic.ListView):
    model = Article
    queryset = Article.objects.all()
    context_object_name = 'articles'


class ArticleView(generic.DetailView):
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HighscoreView(generic.ListView):
    model = HighScores
    queryset = HighScores.objects.values('username').annotate(max_score=Max('score')).order_by('-max_score')
    template_name = 'main/highscore.html'
    context_object_name = 'scores'


def test(request):
    return render_to_response('main/index.html', context={'video': Article.objects.first()})
