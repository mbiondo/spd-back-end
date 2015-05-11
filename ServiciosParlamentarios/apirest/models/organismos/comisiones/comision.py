from __future__ import unicode_literals
from django.db import models
from apirest.models.entidad import Entidad      
from apirest.utils.constants import Constants
        
class Comision(models.Model):    
    id = models.ForeignKey(Entidad, primary_key=True, db_column='comision_id',unique=True)
    caracter = models.TextField(blank=True)
    tipo_camara = models.CharField(max_length=2, blank=True,db_column='tipocamara')
    fecha_inicio = models.DateField(blank=True, null=True,db_column='finicio')
    fecha_fin = models.DateField(blank=True, null=True,db_column='ffin')
    sigla = models.TextField(blank=True)
    norma_creacion = models.TextField(blank=True,db_column='normacreacion')
    
    class Meta:
        managed = False
        db_table = Constants().COMISION
        app_label = Constants().APIREST