from django import forms
from .models import Tarjeta
from django.forms import ValidationError

class TarjetaFormulario(forms.ModelForm):
    
    class Meta:
        model = Tarjeta
        fields = ('rut', 'pri_nom', 'seg_nom', 'pri_ap', 'seg_ap', 'direccion', 'tipo_cliente', 'sexo', 'numero_tarjeta', 'tipo_tarjeta', 'tipo_doc', 'saldo', 'patente',
        'tipo_vehiculo')
        