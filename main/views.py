from django.db.models import Max
from django.shortcuts import render_to_response
from django.views import generic

from main.models import HighScores, Article


class IndexView(generic.TemplateView):
    template_name = 'main/index.html'


class GameView(generic.TemplateView):
    template_name = 'main/game.html'


def handler404(request):
    response = render_to_response('main/404.html', {})
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('main/500.html', {})
    response.status_code = 500
    return response


class HighscoreView(generic.ListView):
    model = HighScores
    queryset = HighScores.objects.values('username').annotate(max_score=Max('score')).order_by('-max_score')
    template_name = 'main/highscore.html'
    context_object_name = 'scores'


def test(request):
    return render_to_response('main/index.html', context={'video': Article.objects.first()})
