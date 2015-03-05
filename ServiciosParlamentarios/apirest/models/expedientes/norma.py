from __future__ import unicode_literals
from django.db import models
from apirest.models.expedientes.comunicacion_pen import ComunicacionPen
from apirest.utils.constants import Constants

class Norma(models.Model):
    id = models.ForeignKey(ComunicacionPen, primary_key=True,db_column='norma_id',unique=True)
    tipo = models.TextField()
    numero = models.CharField(max_length=5, blank=True)
    anio = models.SmallIntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants.NORMA
        app_label = Constants().APIREST
