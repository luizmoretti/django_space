from django.shortcuts import render

from galeria.models import Fotos


def index(request):
    fotos = Fotos.objects.all()
    return render(request, 'galeria/index.html', {"cards": fotos})

def imagem(request):
    return render(request, 'galeria/imagem.html')