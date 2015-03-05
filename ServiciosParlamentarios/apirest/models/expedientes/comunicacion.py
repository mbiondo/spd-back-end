from __future__ import unicode_literals
from django.db import models
from apirest.models.expedientes.expediente import Expediente
from apirest.utils.constants import Constants

class Comunicacion(models.Model):
    id = models.ForeignKey(Expediente, primary_key=True, db_column='comunicacion_id',unique=True)
    subtipo = models.TextField(blank=True)
    fecharecepcion = models.DateField(blank=True, null=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().COMUNICACION
        app_label = Constants().APIREST