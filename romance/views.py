from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Recuerdo, MensajeEspecial, Foto, Musica, Sorpresa
from .forms import FechaAniversarioForm, RecuerdoForm, MensajeEspecialForm, FotoForm, MusicaForm, SorpresaForm

def inicio(request):
    if request.method == 'POST':
        form = FechaAniversarioForm(request.POST)
        if form.is_valid():
            return redirect('dashboard')
        else:
            messages.error(request, 'Fecha incorrecta. Inténtalo de nuevo.')
    else:
        form = FechaAniversarioForm()
    return render(request, 'romance/inicio.html', {'form': form})

def dashboard(request):
    return render(request, 'romance/dashboard.html')

# Vistas para Recuerdos
def recuerdos_lista(request):
    recuerdos = Recuerdo.objects.all().order_by('-fecha')
    return render(request, 'romance/recuerdos_lista.html', {'recuerdos': recuerdos})

def recuerdo_crear(request):
    if request.method == 'POST':
        form = RecuerdoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recuerdo creado exitosamente.')
            return redirect('recuerdos_lista')
    else:
        form = RecuerdoForm()
    return render(request, 'romance/recuerdo_form.html', {'form': form})

def recuerdo_eliminar(request, pk):
    recuerdo = get_object_or_404(Recuerdo, pk=pk)
    recuerdo.delete()
    messages.success(request, 'Recuerdo eliminado exitosamente.')
    return redirect('recuerdos_lista')

# Vistas para Mensajes Especiales
def mensajes_lista(request):
    mensajes = MensajeEspecial.objects.all().order_by('-fecha')
    return render(request, 'romance/mensajes_lista.html', {'mensajes': mensajes})

def mensaje_crear(request):
    if request.method == 'POST':
        form = MensajeEspecialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensaje creado exitosamente.')
            return redirect('mensajes_lista')
    else:
        form = MensajeEspecialForm()
    return render(request, 'romance/mensaje_form.html', {'form': form})

def mensaje_eliminar(request, pk):
    mensaje = get_object_or_404(MensajeEspecial, pk=pk)
    mensaje.delete()
    messages.success(request, 'Mensaje eliminado exitosamente.')
    return redirect('mensajes_lista')

# Vistas para Fotos
def fotos_lista(request):
    fotos = Foto.objects.all().order_by('-fecha')
    return render(request, 'romance/fotos_lista.html', {'fotos': fotos})

def foto_crear(request):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto/Video subido exitosamente.')
            return redirect('fotos_lista')
    else:
        form = FotoForm()
    return render(request, 'romance/foto_form.html', {'form': form})

def foto_eliminar(request, pk):
    foto = get_object_or_404(Foto, pk=pk)
    foto.delete()
    messages.success(request, 'Foto/Video eliminado exitosamente.')
    return redirect('fotos_lista')

# Vistas para Música
def musica_lista(request):
    canciones = Musica.objects.all()
    return render(request, 'romance/musica_lista.html', {'canciones': canciones})

def musica_crear(request):
    if request.method == 'POST':
        form = MusicaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Canción subida exitosamente.')
            return redirect('musica_lista')
    else:
        form = MusicaForm()
    return render(request, 'romance/musica_form.html', {'form': form})

def musica_eliminar(request, pk):
    cancion = get_object_or_404(Musica, pk=pk)
    cancion.delete()
    messages.success(request, 'Canción eliminada exitosamente.')
    return redirect('musica_lista')

# Vista para Sorpresas
def sorpresas(request):
    return render(request, 'romance/sorpresas.html')

# Vista para Flores
def flores(request):
    return render(request, 'romance/flores.html')

# Vista para cambiar modo oscuro
def toggle_dark_mode(request):
    # La lógica de cambio de modo oscuro ahora se maneja en el frontend con JavaScript
    # Simplemente redirigimos de vuelta a la página anterior
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('dashboard')))
