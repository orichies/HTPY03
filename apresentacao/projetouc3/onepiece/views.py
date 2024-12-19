from django.shortcuts import render

# Create your views here.

contexto = {
    'title': 'Unidades - Salão de Beleza Visual da Moda'
}

def onepiece(request):
    return render(
                request,
                'onepiece/index.html',
                )