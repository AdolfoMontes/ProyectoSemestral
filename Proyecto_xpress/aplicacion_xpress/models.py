from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from .choices import tipo_cliente, sexo, tipo_tarjeta, tipo_doc, tipo_vehiculo
# Create your models here.


class Tarjeta(models.Model):
    rut =  models.CharField(max_length=17, null=False, blank=False, unique=True, verbose_name='RUT')
    pri_nom = models.CharField(max_length=30, null=False, blank=False,verbose_name='Primer Nombre')
    seg_nom = models.CharField(max_length=30, verbose_name='Segundo Nombre')
    pri_ap = models.CharField(max_length=30, null=False, blank=False, verbose_name='Apelldo Paterno')
    seg_ap = models.CharField(max_length=30, verbose_name='Apellido Materno')
    direccion = models.CharField(max_length=50,  null=False, blank=False, verbose_name='Dirección')
    tipo_cliente = models.CharField(max_length=1, choices=tipo_cliente, default ='1', verbose_name='Tipo de Cliente')
    sexo = models.CharField(max_length=1, choices=sexo, default='F', verbose_name='Sexo')
    numero_tarjeta =  models.CharField(max_length=17, null=False, blank=False, unique=True, verbose_name='Número de tarjeta')
    tipo_tarjeta = models.CharField(max_length=1, null=False, blank=False, choices=tipo_tarjeta, default = '1', verbose_name='Tipo de tarjeta')
    tipo_doc = models.CharField(max_length=1, null=True, blank=True, choices=tipo_doc,  verbose_name='Tipo de documento ')
    saldo = models.IntegerField(default=0, null=False, blank=False)
    patente = models.CharField(max_length=16, null=True, blank=False, unique=True, verbose_name='Patente')
    tipo_vehiculo = models.CharField(max_length=30, choices=tipo_vehiculo, default='1', verbose_name='Tipo de vehiculo')
    fecha_creacion = models.DateTimeField(
        default=timezone.now, null=False, verbose_name='Fecha de creación')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.numero_tarjeta
    
    class Meta:
        verbose_name='tarjeta'
        verbose_name_plural='tarjetas'
        db_table='tarjeta'

