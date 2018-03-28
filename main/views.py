from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/index.html'


class GameView(TemplateView):
    template_name = 'main/game.html'


def handler404(request):
    response = render_to_response('main/404.html', {})
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('main/500.html', {})
    response.status_code = 500
    return response
