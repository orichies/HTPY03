from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.

def outros(request):
    # lista = '<ol><li>Putchelo</li><li>Juan</li></ol>'
    return render(request,'outros/index.html')

def atividade(request):
    return render(request,'outros/atividade.html')
