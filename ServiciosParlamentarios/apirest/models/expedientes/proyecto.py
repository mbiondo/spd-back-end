from __future__ import unicode_literals
from django.db import models
from apirest.models.expedientes.expediente import Expediente
from apirest.utils.constants import Constants

class Proyecto(models.Model):
    id = models.ForeignKey(Expediente, primary_key=True,db_column='proyecto_id',unique=True)
    fk_proyecto_reproduce = models.ForeignKey('self', db_column='fk_proyecto_reproduce', blank=True, null=True)
    estado = models.TextField(blank=True)
    tipo_proy = models.TextField(blank=True,db_column='tipoproy')
    subtipo_proy = models.TextField(blank=True,db_column='subtipoproy')
    codigo_digesto = models.CharField(max_length=6, blank=True,db_column='codigodigesto')
    
    class Meta:
        managed = False
        db_table = Constants().PROYECTO
        app_label = Constants().APIREST