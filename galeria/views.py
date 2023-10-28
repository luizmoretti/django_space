from django.shortcuts import render, get_object_or_404

from galeria.models import Fotos


def index(request):
    fotos = Fotos.objects.order_by('data_fotografia').filter(publicada=True)
    
    return render(request, 'galeria/index.html', {"cards": fotos})

def imagem(request, foto_id):
    fotos =  get_object_or_404(Fotos, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"foto": fotos })

def buscar(request):
    fotos = Fotos.objects.order_by('data_fotografia').filter(publicada=True)
    
    if 'buscar' in request.GET:
        nome = request.GET['buscar']
        if nome:
            fotos = fotos.filter(nome__icontains=nome)
    
    return render(request, 'galeria/buscar.html', {"cards": fotos})