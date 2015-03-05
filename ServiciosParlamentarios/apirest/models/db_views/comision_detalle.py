from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class ComisionesDetalle(models.Model):
    nombre_comision = models.TextField(blank=True, primary_key = True)
    nombre_corto = models.TextField(blank=True)
    comision_id = models.IntegerField(blank=True, null=True)
    caracter = models.CharField(max_length=1, blank=True)
    tipocamara = models.CharField(max_length=2, blank=True)
    finicio = models.DateField(blank=True, null=True)
    ffin = models.DateField(blank=True, null=True)
    sigla = models.TextField(blank=True)
    normacreacion = models.TextField(blank=True)
    nombre_legislador = models.TextField(blank=True)
    cargo = models.TextField(blank=True)
    estado = models.CharField(max_length=1, blank=True)
    fdesde = models.DateTimeField(blank=True, null=True)
    fhasta = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().COMISIONES_DETALLE
        app_label = Constants().APIREST                      