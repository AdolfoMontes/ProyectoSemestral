# Generated by Django 3.2.4 on 2021-07-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_xpress', '0004_alter_tarjeta_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjeta',
            name='seg_ap',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Apellido Materno'),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='seg_nom',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Segundo Nombre'),
        ),
    ]