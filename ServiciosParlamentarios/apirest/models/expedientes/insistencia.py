from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.resultado import Resultado

class Insistencia(Resultado):
    
    insistencia = models.OneToOneField(Resultado, parent_link=True, related_name='insistencias')
    articulos = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().INSISTENCIA
        app_label = Constants().APIREST
