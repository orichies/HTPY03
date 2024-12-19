from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.

contexto = {
    'title': 'Home - Salão de Beleza Visual da Moda'
}

def home(request):
    return render(request, 
                  'home/index.html',
                contexto
                 )