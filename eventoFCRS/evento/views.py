from django.shortcuts import render
from django.http import HttpResponse
from evento.models import Evento

def index(request):
    evento = Evento.objects.all()
    return render(request, 'evento/home.html', {'lista_eventos' : evento})
