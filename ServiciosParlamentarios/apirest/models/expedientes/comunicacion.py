from __future__ import unicode_literals
from django.db import models
from apirest.models.expedientes.expediente import Expediente
from apirest.utils.constants import Constants

class Comunicacion(Expediente):
    
    comunicacion = models.OneToOneField(Expediente, parent_link=True)
    subtipo = models.TextField(blank=True)
    fecha_recepcion = models.DateField(blank=True, null=True, db_column='fecharecepcion')
    orden = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().COMUNICACION
        app_label = Constants().APIREST
        