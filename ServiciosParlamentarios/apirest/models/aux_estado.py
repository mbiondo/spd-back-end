from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class AuxEstado(models.Model):
    id = models.IntegerField(primary_key=True, db_column='aux_estado_id')
    valor = models.TextField(blank=True)
    entidad = models.TextField(blank=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True)
    fdesde = models.DateTimeField(blank=True, null=True)
    fhasta = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().AUX_ESTADO
        app_label = Constants().APIREST    