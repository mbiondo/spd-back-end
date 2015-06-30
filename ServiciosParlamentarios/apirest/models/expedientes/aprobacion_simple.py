from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.resultado import Resultado

class AprobacionSimple(Resultado):
    
    aprobacion_simple = models.OneToOneField(Resultado, parent_link=True, related_name='aprobaciones_simples')
    numero = models.SmallIntegerField(blank=True, null=True)
    anio = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().APROBACION_SIMPLE
        app_label = Constants().APIREST