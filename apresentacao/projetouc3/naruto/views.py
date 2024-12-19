from django.shortcuts import render

# Create your views here.

def naruto(request):
    return render(
                request,
                'naruto/index.html',
                )
