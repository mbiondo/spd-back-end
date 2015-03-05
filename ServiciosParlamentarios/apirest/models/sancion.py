from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.resultado import Resultado

class Sancion(models.Model):
    id = models.ForeignKey(Resultado, primary_key=True, db_column='sancion_definitiva_id',unique=True)
    nroley = models.CharField(max_length=5, blank=True)
    sancionpromulgada = models.TextField(blank=True)
    sancionvetada = models.TextField(blank=True)
    codigodigesto = models.TextField(blank=True)
    binsistida = models.CharField(max_length=1, blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().SANCION
        app_label = Constants().APIREST