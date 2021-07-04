from django.shortcuts import render
from .models import Tarjeta
from .forms import TarjetaFormulario
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

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
    
def portalGestion(request):
    return render(request, 'aplicacion/portal/admin/portaladministracion.html', {})
    
def lista_tarjetas(request):
    tarjetas = Tarjeta.objects.all()
    return render(request, 'aplicacion/portal/admin/listartarjeta.html', {'tarjetas':tarjetas})
    

def crearTarjetas(request):
    tarjeta = Tarjeta()
    formulario = TarjetaFormulario()
    
    if request.method == 'POST':
        nuevaTarjeta = TarjetaFormulario(request.POST, instance=tarjeta)
        if nuevaTarjeta.is_valid():
            try:
                nuevaTarjeta.save()
                messages.add_message(request, messages.INFO, 'Tarjeta creada correctamente!')
            except:
                messages.add_message(request, messages.INFO, 'No se pudo crear la tarjeta, verifíca que el usuario no exista y que todos los campos son correctos')
        else:
            messages.add_message(request, messages.INFO, 'No se pudo crear la tarjeta, verifíca que el usuario no exista y que todos los campos son correctos')
        return render (request, 'aplicacion/portal/admin/creartarjeta.html', {'formulario': formulario})
        
    else:
        return render (request, 'aplicacion/portal/admin/creartarjeta.html', {'formulario': formulario})

def modificarTarjeta(request, pk):
    tarjeta = get_object_or_404(Tarjeta, pk=pk)
    if request.method == "POST":
        modificarTarjeta = TarjetaFormulario(request.POST, instance=tarjeta)
        if modificarTarjeta.is_valid():
            tarjeta = modificarTarjeta.save(commit=False)
            tarjeta.creador = request.user
            tarjeta.save()
            tarjetas = Tarjeta.objects.all()
            return render(request, 'aplicacion/portal/admin/listartarjeta.html', {'tarjetas': tarjetas})
    else:
        modificarTarjeta = TarjetaFormulario(instance=tarjeta)
    return render(request, 'aplicacion/portal/admin/modificarTarjeta.html', {'modificarTarjeta': modificarTarjeta})     


def busqueda(request):
   q = request.GET.get('q', '')
   tarjetas = Tarjeta.objects.filter(rut__icontains=q)
   return render(request, 'aplicacion/portal/admin/listartarjeta.html', {'tarjetas': tarjetas})
   
   
   
   
   