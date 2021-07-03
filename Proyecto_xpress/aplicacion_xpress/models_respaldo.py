from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from .choices import tipo_cliente, sexo, tipo_tarjeta, tipo_doc, tipo_vehiculo
# Create your models here.



class Cliente(models.Model):
    cod_cliente =  models.CharField(max_length=17, null=False, blank=False, unique=True, verbose_name='Código cliente')
    pri_nom = models.CharField(max_length=30, null=False, blank=False,verbose_name='Primer Nombre')
    seg_nom = models.CharField(max_length=30, null=True, blank=True, verbose_name='Segundo Nombre')
    pri_ap = models.CharField(max_length=30, null=False, blank=False, verbose_name='Apelldo Paterno')
    seg_ap = models.CharField(max_length=30, null=True, blank=True, verbose_name='Apellido Materno')
    direccion = models.CharField(max_length=50, verbose_name='Dirección')
    tipo_cliente = models.CharField(max_length=1, choices=tipo_cliente, default ='1', verbose_name='Tipo de Cliente')
    sexo = models.CharField(max_length=1, choices=sexo, default='F', verbose_name='Sexo')
    fecha_creacion = models.DateTimeField(
        default=timezone.now, null=False, verbose_name='Fecha de Creación')

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def nombreCompleto(self):
        return ("{} {}, {}". format(self.pri_ap, self.seg_ap, self.pri_nom ))

    def __str__(self):
        return self.nombreCompleto()
        
    class Meta:
        verbose_name='cliente'
        verbose_name_plural='clientes'
        db_table='cliente'
        ordering=['cod_cliente']


class Tarjeta(models.Model):
    numero_tarjeta =  models.CharField(max_length=17, null=False, blank=False, unique=True, verbose_name='Número de tarjeta')
    tipo_tarjeta = models.CharField(max_length=1, null=False, blank=False, choices=tipo_tarjeta, default = '1', verbose_name='Tipo de tarjeta')
    tipo_doc = models.CharField(max_length=1, null=True, blank=True, choices=tipo_doc,  verbose_name='Tipo de documento ')
    saldo = models.IntegerField(default=0, null=False, blank=False)
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
       
        
class Vehiculo(models.Model):
    patente = models.CharField(max_length=16, null=False, blank=False, unique=True, verbose_name='Patente')
    tipo_vehiculo = models.CharField(max_length=30, choices=tipo_vehiculo, default='1', verbose_name='Tipo de vehiculo')
    fecha_creacion = models.DateTimeField(
        default=timezone.now, null=False, verbose_name='Fecha de creación')
    usuario = models.ForeignKey(Cliente, null=True, blank=True, on_delete = models.CASCADE, verbose_name='Usuario')
    modelo = models.CharField(max_length=40, verbose_name='Modelo')
    tarjeta = models.ForeignKey(Tarjeta, null=True, blank=True, unique=True, on_delete = models.CASCADE, verbose_name='Tarjeta')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.patente
        
    class Meta:
        verbose_name='vehiculo'
        verbose_name_plural='vehiculos'
        db_table='vehiculo'
       
