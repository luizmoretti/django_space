from django.urls import path
from .views import index, imagem


urlpatterns = [
    path('home/', index, name='index'),
    path('imagem/', imagem, name='imagem')
]