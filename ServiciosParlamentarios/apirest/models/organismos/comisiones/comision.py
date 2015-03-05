from __future__ import unicode_literals
from django.db import models
from apirest.models.entidad import Entidad      
from apirest.utils.constants import Constants
        
class Comision(models.Model):    
    id = models.ForeignKey(Entidad, primary_key=True, db_column='comision_id',unique=True)
    caracter = models.TextField(blank=True)
    tipocamara = models.CharField(max_length=2, blank=True)
    finicio = models.DateField(blank=True, null=True)
    ffin = models.DateField(blank=True, null=True)
    sigla = models.TextField(blank=True)
    normacreacion = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().COMISION
        app_label = Constants().APIREST