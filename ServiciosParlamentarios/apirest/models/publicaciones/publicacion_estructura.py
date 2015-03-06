from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class PublicacionEstructura(models.Model):
    id = models.AutoField(primary_key=True,db_column='publicacion_estructura_id')
    descripcion = models.TextField(blank=True)
    fdesde = models.DateField(blank=True, null=True)
    fhasta = models.DateField(blank=True, null=True)
    tipo = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().PUBLICACION_ESTRUCTURA
        app_label = Constants().APIREST