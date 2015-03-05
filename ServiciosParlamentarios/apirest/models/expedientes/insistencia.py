from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.resultado import Resultado

class Insistencia(models.Model):
    id = models.ForeignKey(Resultado, primary_key=True, db_column='insistencia_id',unique=True)
    tipo = models.TextField(blank=True)
    articulos = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = Constants().INSISTENCIA
        app_label = Constants().APIREST
