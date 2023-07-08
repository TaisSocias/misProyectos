from django.shortcuts import render, redirect, get_object_or_404
from .models import Artista,Especialidad, Obra, Contacto
from .forms import ContactoForm, ObraForm
# Create your views here.

# vistas del menú
def index(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/index.html ', context)

def nosotros(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/nosotros.html ', context)

def anunciosEs(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/anunciosEs.html ', context)

def anunciosPi(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/anunciosPi.html ', context)

def anunciosTej(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/anunciosTej.html', context)

def anunciosOrf(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/anunciosOrf.html ', context)

def blog(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/blog.html ', context)

def contacto(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/contacto.html ', context)

def TejMuralla(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/TejMuralla.html ', context)

def TejCorazon(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/TejCorazon.html ', context)

def TejCoral(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/TejCoral.html ', context)

def PiSwing(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/PiSwing.html ', context)

def PiNoche(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/PiNoche.html ', context)

def Pimona(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/Pimona.html ', context)

def OrfTutanmamon(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/OrfTutanmamon.html ', context)

def OrfRam(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/OrfRam.html ', context)

def OrfMaikol(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/OrfMaikol.html ', context)

def EsVenus(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/EsVenus.html ', context)

def EsSirena(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/EsSirena.html ', context)

def EsEstatua(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/EsEstatua.html ', context)

def EsEsfinge(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/EsEsfinge.html ', context)

def EsDavid(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/EsDavid.html ', context)

def EsCristo(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/EsCristo.html ', context)

def BlogOrfebreria(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/BlogOrfebreria.html ', context)

def BlogTejido(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/BlogTejido.html ', context)

def BlogTejido2(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/BlogTejido2.html ', context)

def BlogPintura(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/BlogPintura.html ', context)

def BlogEscultura(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/BlogEscultura.html ', context)

def BlogArte(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/BlogArte.html ', context)

def base(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/base.html ', context)

def anuncio(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/anuncio.html ', context)

def entrada(request):
    artistas = Artista.objects.all()
    context={"artistas":artistas}
    return render(request, 'artistas/entrada.html ', context)

def listadoSQL(request):
    artistas= Artista.objects.raw('SELECT * FROM artistas_Artista')
    print(artistas)
    context={"artistas":artistas}
    return render(request, 'artistas/index.html', context)

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Consulta enviada"
        else:
            data["form"] = formulario
    return render(request, 'artistas/contacto.html', data)

def agregar_obra(request):

    data = {
        'form': ObraForm()
    }

    if request.method == 'POST':
        formulario = ObraForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Obra guardada correctamente"
        else:
            data["form"] = formulario
    return render(request, 'artistas/agregar.html', data)

def listar_obra(request):
    obra = Obra.objects.all()

    data = {
        'obra' : obra
    }
    return render(request, 'artistas/listar.html', data)

def modificar_obra(request, id):
    nombre_obra = get_object_or_404(Obra, id_obra=id)

    data = {
        'form': ObraForm(instance=nombre_obra)
    }

    if request.method == 'POST':
        formulario = ObraForm(data=request.POST, instance=nombre_obra, files=request.FILES)  # Corregir esta línea
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_obra")
        data["form"] = formulario

    return render(request, 'artistas/modificar.html', data)

def eliminar_obra(request, id):
    nombre_obra = get_object_or_404(Obra, id_obra=id)
    nombre_obra.delete()
    return redirect(to="listar_obra")
