from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.resultado import Resultado

class AprobacionSimple(models.Model):
    id = models.ForeignKey(Resultado, primary_key=True, db_column='aprobacion_simple_id',unique=True)
    tipo = models.TextField(blank=True)
    numero = models.SmallIntegerField(blank=True, null=True)
    anio = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = Constants().APROBACION_SIMPLE
        app_label = Constants().APIREST