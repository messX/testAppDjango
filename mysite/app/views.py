import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from mysite.app.models import Movie, MovieToActor


def index(request):
    movie_name = request.GET.get('name')
    movie = Movie.objects.get(name=movie_name)
    movie_to_actor = [rec.actor.as_json() for rec in MovieToActor.objects.filter(movie=movie)]
    return HttpResponse(json.dumps({"actors":movie_to_actor}),
                                content_type='application/json')