from django.shortcuts import render
from .models import Artista,Especialidad, Obra

# Create your views here.

def index(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/index.html', context)

def listadoSQL(request):
    artistas= Artista.objects.raw('SELECT * FROM artistas_Artista')
    print(artistas)
    context={"artistas":artistas}
    return render(request, 'artistas/index.html', context)

def crud(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/artistas_list.html', context)

