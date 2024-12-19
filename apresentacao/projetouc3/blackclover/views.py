from django.shortcuts import render

# Create your views here.

def blackclover(request):
    return render(
                request,
                'blackclover/index.html',
                )
