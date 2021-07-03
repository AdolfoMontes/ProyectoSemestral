from django.shortcuts import render
from .models import Tarjeta
from django.contrib import messages
# Create your views here.



def index(request):
    return render(request, 'aplicacion/index.html', {})
    
    
def ayuda(request):
    return render(request, 'aplicacion/ayuda.html', {})
    
def comparador(request):
    return render(request, 'aplicacion/comparador.html', {})
    
def contacto(request):
    return render(request, 'aplicacion/contacto.html', {})
    
def portal(request):
    return render(request, 'aplicacion/portal.html', {})
    
def productos(request):
    return render(request, 'aplicacion/productos.html', {})
    
def registro(request):
    return render(request, 'aplicacion/registro.html', {})
    
def seguros(request):
    return render(request, 'aplicacion/seguros.html', {})
    
def sucursales(request):
    return render(request, 'aplicacion/sucursales.html', {})
    
def portalTarjetas(request):
    return render(request, 'aplicacion/portal/tarjetas.html', {})
    
    
def lista_tarjetas(request):
    tarjetas = Tarjeta.objects.all()
    return render(request, 'aplicacion/portal/admin/listartarjeta.html', {'tarjetas':tarjetas})