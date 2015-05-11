from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Evento(models.Model):
    id = models.AutoField(primary_key=True,db_column='evento_id')
    nombre = models.TextField(blank=True)
    nombre_corto = models.TextField(blank=True,db_column='nombrecorto')
    fecha_inicio = models.DateTimeField(blank=True, null=True,db_column='finicio')
    fecha_fin = models.DateTimeField(blank=True, null=True,db_column='ffin')
    tipo = models.TextField(blank=True)
    estado = models.TextField(blank=True)
    visibilidad = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().EVENTO
        app_label = Constants().APIREST
