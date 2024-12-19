from django.shortcuts import render

# Create your views here.

def tokyoghoul(request):
    return render(
                request,
                'tokyoghoul/index.html',
                )