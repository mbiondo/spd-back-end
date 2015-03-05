from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.debate import Debate
from apirest.models.expedientes.expediente import Expediente

class DebateSobreExpediente(models.Model):
    id = models.IntegerField(primary_key=True,db_column='debate_sobre_expediente_id')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    fk_debate = models.ForeignKey(Debate, db_column='fk_debate')
    orden = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().DEBATE_SOBRE_EXPEDIENTE
        app_label = Constants().APIREST