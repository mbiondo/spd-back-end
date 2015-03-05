from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class ExpedienteTramitacion(models.Model):
    codigoexp = models.CharField(max_length=14, blank=True)
    tramite_id = models.IntegerField(blank=True, null=True)
    tipo_tramite = models.TextField(blank=True)
    expediente_id = models.IntegerField(blank=True, null=True)
    tipo = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)
    fecha = models.DateTimeField(blank=True, null=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    resultado = models.TextField(blank=True)
    camara = models.TextField(blank=True)
    nro_ley = models.CharField(max_length=-1, blank=True)

    class Meta:
        managed = False
        db_table = Constants().EXPEDIENTE_TRAMITACION
        app_label = Constants().APIREST
