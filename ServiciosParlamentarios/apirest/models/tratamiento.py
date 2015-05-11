from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Tratamiento(models.Model):
    id = models.AutoField(primary_key=True,db_column='tratamiento_id')
    tipo = models.TextField(blank=True)
    orden = models.IntegerField(blank=True, null=True)
    resumen = models.TextField(blank=True)
    fuera_de_temario = models.CharField(max_length=1, blank=True,db_column='bfueradetemario')
    sobre_tablas = models.CharField(max_length=1, blank=True,db_column='bsobretablas')
    
    class Meta:
        managed = False
        db_table = Constants().TRATAMIENTO
        app_label = Constants().APIREST