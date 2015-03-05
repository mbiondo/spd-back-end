from __future__ import unicode_literals
from django.db import models
from apirest.models.expedientes.expediente import Expediente
from apirest.utils.constants import Constants

class ComunicacionLeg(models.Model):
    id = models.ForeignKey(Expediente, primary_key=True, db_column='comunicacion_leg_id',unique=True)
    subtipo = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().COMUNICACION_LEG
        app_label = Constants().APIREST