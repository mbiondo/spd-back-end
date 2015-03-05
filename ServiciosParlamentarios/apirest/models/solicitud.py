from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.expediente import Expediente

class Solicitud(models.Model):
    id = models.ForeignKey(Expediente, primary_key=True, db_column='solicitud_id',unique=True)
    subtipo = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().SOLICITUD
        app_label = Constants().APIREST