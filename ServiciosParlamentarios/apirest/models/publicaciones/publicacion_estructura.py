from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class PublicacionEstructura(models.Model):
    id = models.AutoField(primary_key=True,db_column='publicacion_estructura_id')
    descripcion = models.TextField(blank=True)
    fecha_desde = models.DateField(blank=True, null=True,db_column='fdesde')
    fecha_hasta = models.DateField(blank=True, null=True,db_column='fhasta')
    tipo = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().PUBLICACION_ESTRUCTURA
        app_label = Constants().APIREST