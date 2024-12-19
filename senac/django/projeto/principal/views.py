from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.

def principal(request):
    # lista = '<ol><li>Putchelo</li><li>Juan</li></ol>'
    return render(request,'principal/index.html')

