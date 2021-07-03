from django.urls import path, include
from .import views


urlpatterns = [
  path('', views.index),
  path('ayuda.html', views.ayuda),
  path('comparador.html', views.comparador),
  path('contacto.html', views.contacto),
  path('portal.html', views.portal),
  path('productos.html', views.productos),
  path('registro.html', views.registro),
  path('seguros.html', views.seguros),
  path('sucursales.html', views.sucursales),
  path('portal/tarjetas.html', views.portalTarjetas),
  path('portal/admin/listartarjeta.html', views.lista_tarjetas)
]