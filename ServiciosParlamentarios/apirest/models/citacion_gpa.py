from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.aux_estado import AuxEstado

class CitacionGpa(models.Model):
    id = models.IntegerField(primary_key=True, db_column='citacion_gpa_id')
    fecha = models.DateTimeField(blank=True, null=True)
    fk_lugar = models.ForeignKey('Lugar', db_column='fk_lugar', blank=True, null=True)
    fk_estado = models.ForeignKey(AuxEstado, db_column='fk_estado', blank=True, null=True)
    resumen = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    visibilidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().CITACION_GPA
        app_label = Constants().APIREST        