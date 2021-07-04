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
  path('verTarjetas', views.lista_tarjetas),
  path('portalGestion', views.portalGestion, name='portal_gestion'),
  path('crearTarjetas', views.crearTarjetas),
  path('tarjeta/<int:pk>/edit/', views.modificarTarjeta, name='editar_tarjeta'),
  path('buscador', views.busqueda),
]