from django.shortcuts import render


def index(request):
    dados = {
    1: {"Nome": "Nebulosa de Carina",
        "legenda": "webtelescop.org / NASA / James Webb"},
    
    2: {"Nome": "Galaxia  NGC 1079",
        "legenda": "nasa.org / NASA / Hublle"},
}
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')