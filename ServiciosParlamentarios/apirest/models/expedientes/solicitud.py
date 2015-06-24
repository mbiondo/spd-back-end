from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.expediente import Expediente

class Solicitud(Expediente):
    
    solicitud = models.OneToOneField(Expediente, parent_link=True)
    subtipo = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().SOLICITUD
        app_label = Constants().APIREST