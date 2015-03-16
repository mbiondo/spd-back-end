from __future__ import unicode_literals

from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.expediente import Expediente

class Proyectos (models.Model):
    expediente_id = models.ForeignKey(Expediente,db_column='expediente_id',related_name='proyectos',primary_key=True)
    codigoexp = models.CharField(max_length=14, blank=True)
    codigonum = models.CharField(max_length=5, blank=True)
    codigoorigen = models.CharField(max_length=3, blank=True)
    codigoanio = models.CharField(max_length=4, blank=True)
    sumario = models.TextField(blank=True)
    tipocamara = models.TextField(blank=True)
    tipo = models.TextField(blank=True)
    codigoestado = models.SmallIntegerField(blank=True, null=True)  
    fechacaducidad = models.DateField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    periodo = models.SmallIntegerField(blank=True, null=True)
    titulo = models.TextField(blank=True)
    voces = models.TextField(blank=True)
    resultado = models.TextField(blank=True)
    tipoproy = models.TextField(blank=True)
    nroley = models.CharField(max_length=-1, blank=True)

    class Meta:
        managed = False
        db_table = Constants().PROYECTOS
        app_label = Constants().APIREST
    
