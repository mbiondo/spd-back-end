from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.expediente import Expediente

class ExpedienteReferidoExpediente(models.Model):
    id = models.AutoField(primary_key=True,db_column='expediente_referido_expediente_id')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    fk_expediente_referido = models.ForeignKey(Expediente, db_column='fk_expediente_referido')

    class Meta:
        managed = False
        db_table = Constants().EXPEDIENTE_REFERIDO_EXPEDIENTE
        app_label = Constants().APIREST

