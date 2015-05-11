from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Interbloque(models.Model):
    id = models.AutoField(primary_key=True,db_column='interbloque_id')
    nombre = models.TextField()
    caracter = models.TextField(blank=True)
    fecha_inicio = models.DateField(blank=True, null=True,db_column='finicio')
    fecha_fin = models.DateField(blank=True, null=True,db_column='ffin')
    
    class Meta:
        managed = False
        db_table = Constants().INTERBLOQUE
        app_label = Constants().APIREST      