from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Evento(models.Model):
    id = models.IntegerField(primary_key=True,db_column='evento_id')
    nombre = models.TextField(blank=True)
    nombrecorto = models.TextField(blank=True)
    finicio = models.DateTimeField(blank=True, null=True)
    ffin = models.DateTimeField(blank=True, null=True)
    tipo = models.TextField(blank=True)
    estado = models.TextField(blank=True)
    visibilidad = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().EVENTO
        app_label = Constants().APIREST
