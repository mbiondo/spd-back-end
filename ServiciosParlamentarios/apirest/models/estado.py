from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.expediente import Expediente

class Estado(models.Model):
    id = models.AutoField(primary_key=True,db_column='estado_id')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    descripcion = models.TextField()
    finicio = models.DateTimeField(blank=True, null=True)
    ffin = models.DateTimeField(blank=True, null=True)
    observaciones = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().ESTADO
        app_label = Constants().APIREST

