from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.evento import Evento

class EventoReunion(models.Model):
    id = models.AutoField(primary_key=True,db_column='evento_reunion_id')
    fk_evento = models.ForeignKey(Evento, db_column='fk_evento')
    fecha_inicio = models.DateTimeField(blank=True, null=True,db_column='finicio')
    fecha_fin = models.DateTimeField(blank=True, null=True,db_column='ffin')
    lugar = models.TextField(blank=True)
    estado = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().EVENTO_REUNION
        app_label = Constants().APIREST
