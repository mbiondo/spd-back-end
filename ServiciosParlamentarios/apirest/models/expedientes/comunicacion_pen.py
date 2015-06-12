from __future__ import unicode_literals
from django.db import models
from apirest.models.expedientes.expediente import Expediente
from apirest.utils.constants import Constants

class ComunicacionPen(Expediente):
    
    comunicacion_pen = models.OneToOneField(Expediente,parent_link=True)
    subtipo = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().COMUNICACION_PEN
        app_label = Constants().APIREST