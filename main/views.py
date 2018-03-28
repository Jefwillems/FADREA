from django.shortcuts import render_to_response
from django.views import generic

from main.models import HighScores


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
    queryset = HighScores.objects.order_by('-score', 'username')
    template_name = 'main/highscore.html'
    context_object_name = 'scores'
