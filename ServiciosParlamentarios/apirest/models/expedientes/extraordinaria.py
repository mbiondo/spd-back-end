from __future__ import unicode_literals
from django.db import models
from apirest.models.expedientes.comunicacion_pen import ComunicacionPen
from apirest.utils.constants import Constants

class Extraordinaria(models.Model):
    id = models.ForeignKey(ComunicacionPen, primary_key=True, db_columns='extraordinaria_id', unique=True)
    
    class Meta:
        managed = False
        db_table = Constants().EXTRAORDINARIA
        app_label = Constants().APIREST
