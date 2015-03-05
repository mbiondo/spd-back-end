from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Planteamiento(models.Model):
    id = models.IntegerField(primary_key=True,db_column='planteamiento_id')
    tipo = models.TextField(blank=True)
    sumario = models.TextField(blank=True)
    orden = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().PLANTEAMIENTO
        app_label = Constants().APIREST        
