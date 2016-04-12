from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'evento/home.html',{
    'nome': "Marcos Douglas",
    'idade':"18 anos",
    'altura':"1,68 metros",
    })
