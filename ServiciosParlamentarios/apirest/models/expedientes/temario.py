from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.comunicacion_pen import ComunicacionPen

class Temario(models.Model):
    id = models.ForeignKey(ComunicacionPen, primary_key=True, db_column='temario_id', unique=True)
    
    class Meta:
        managed = False
        db_table = Constants().TEMARIO
        app_label = Constants().APIREST