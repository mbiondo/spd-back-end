from __future__ import unicode_literals
from django.db import models
from apirest.models.entidad import Entidad
from apirest.models.expedientes.expediente import Expediente
from apirest.utils.constants import Constants

class EntidadProduceExpediente(models.Model):
    id = models.IntegerField(primary_key=True,db_column='entidad_produce_expediente_id')
    fk_entidad = models.ForeignKey(Entidad, db_column='fk_entidad')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    class Meta:
        managed = False
        db_table = Constants().ENTIDAD_PRODUCE_EXPEDIENTE
        app_label = Constants().APIREST