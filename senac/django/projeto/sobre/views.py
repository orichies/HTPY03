from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.

def sobre(request):
    # lista = '<ol><li>Putchelo</li><li>Juan</li></ol>'
    return render(request,'sobre/index.html')

def produtos(request):
    # lista = '<ol><li>Putchelo</li><li>Juan</li></ol>'
    return render(request,'sobre/index.html')

def servicos(request):
    # lista = '<ol><li>Putchelo</li><li>Juan</li></ol>'
    return render(request,'sobre/index.html')
