from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
                
class BloqueDetalle(models.Model):
    bloque_id = models.IntegerField(blank=True, null=True, primary_key = True)
    nombre = models.TextField(blank=True)
    nrointegrantes = models.SmallIntegerField(blank=True, null=True)
    finicio = models.DateField(blank=True, null=True)
    ffin = models.DateField(blank=True, null=True)
    tipocamara = models.CharField(max_length=1, blank=True)
    nota = models.TextField(blank=True)
    sigla = models.TextField(blank=True)
    nombre_legislador = models.TextField(blank=True)
    cargo = models.TextField(blank=True)
    jerarquia = models.SmallIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)
    fdesde = models.DateTimeField(blank=True, null=True)
    fhasta = models.DateTimeField(blank=True, null=True)
    cargo_legislador = models.TextField(blank=True)
    partido = models.TextField(blank=True)
    finicio_legislador = models.DateField(blank=True, null=True)
    ffin_legislador = models.DateField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().BLOQUE_DETALLE
        app_label = Constants().APIREST      