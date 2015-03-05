from __future__ import unicode_literals
from django.db import models
from apirest.models.entidad import Entidad
from apirest.utils.constants import Constants
        
class Bloque(models.Model):
    id = models.ForeignKey(Entidad, primary_key=True,db_column='bloque_id',unique=True)
    nombre = models.TextField(blank=True)
    nrointegrantes = models.SmallIntegerField(blank=True, null=True)
    finicio = models.DateField(blank=True, null=True)
    ffin = models.DateField(blank=True, null=True)
    tipocamara = models.CharField(max_length=1, blank=True)
    nota = models.TextField(blank=True)
    sigla = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().BLOQUE
        app_label = Constants().APIREST        