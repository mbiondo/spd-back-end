from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class EstadoExpediente(models.Model):
    id = models.AutoField(primary_key=True,db_column='estado_expediente_id')
    fk_expediente = models.ForeignKey('Expediente', db_column='fk_expediente')
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField(blank=True, null=True,db_column='finicio')
    fecha_fin = models.DateTimeField(blank=True, null=True,db_column='ffin')
    observaciones = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().ESTADO_EXPEDIENTE
        app_label = Constants().APIREST

