from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.expediente import Expediente
from apirest.models.planteamiento import Planteamiento

class PlanteamientoReferidoExpediente(models.Model):
    id = models.IntegerField(primary_key=True,db_column='planteamiento_referido_expediente_id')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    fk_planteamiento = models.ForeignKey(Planteamiento, db_column='fk_planteamiento')

    class Meta:
        managed = False
        db_table = Constants().PLANTEAMIENTO_REFERIDO_EXPEDIENTE
        app_label = Constants().APIREST