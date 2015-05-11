from __future__ import unicode_literals

from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.expediente import Expediente

class Proyectos (models.Model):
    expediente_id = models.ForeignKey(Expediente,db_column='expediente_id',related_name='proyectos',primary_key=True)
    codigo_exp = models.CharField(max_length=14, blank=True,db_column='codigoexp')
    codigo_num = models.CharField(max_length=5, blank=True,db_column='codigonum')
    codigo_origen = models.CharField(max_length=3, blank=True,db_column='codigoorigen')
    codigo_anio = models.CharField(max_length=4, blank=True,db_column='codigoanio')
    sumario = models.TextField(blank=True)
    tipo_camara = models.TextField(blank=True,db_column='tipocamara')
    tipo = models.TextField(blank=True)
    codigo_estado = models.SmallIntegerField(blank=True, null=True,db_column='codigoestado')  
    fecha_caducidad = models.DateField(blank=True, null=True,db_column='fechacaducidad')
    fecha = models.DateField(blank=True, null=True)
    periodo = models.SmallIntegerField(blank=True, null=True)
    titulo = models.TextField(blank=True)
    voces = models.TextField(blank=True)
    resultado = models.TextField(blank=True)
    tipo_proy = models.TextField(blank=True,db_column='tipoproy')
    nro_ley = models.CharField(max_length=-1, blank=True,db_column='nroley')

    class Meta:
        managed = False
        db_table = Constants().PROYECTOS
        app_label = Constants().APIREST
    
