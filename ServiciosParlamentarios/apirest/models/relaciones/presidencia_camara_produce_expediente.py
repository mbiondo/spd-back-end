from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.presidencia import PresidenciaCamara
from apirest.models.expedientes.expediente import Expediente

class PresidenciaCamaraProduceExpediente(models.Model):
    id = models.AutoField(primary_key=True,db_column='presidencia_camara_produce_expediente_id')
    fk_presidencia_camara = models.ForeignKey(PresidenciaCamara, db_column='fk_presidencia_camara')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente', unique=True)

    class Meta:
        managed = False
        db_table = Constants().PRESIDENCIA_CAMARA_PRODUCE_EXPEDIENTE
        app_label = Constants().APIREST        