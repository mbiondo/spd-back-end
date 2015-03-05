from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Interbloque(models.Model):
    id = models.IntegerField(primary_key=True,db_column='interbloque_id')
    nombre = models.TextField()
    caracter = models.TextField(blank=True)
    finicio = models.DateField(blank=True, null=True)
    ffin = models.DateField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().INTERBLOQUE
        app_label = Constants().APIREST      