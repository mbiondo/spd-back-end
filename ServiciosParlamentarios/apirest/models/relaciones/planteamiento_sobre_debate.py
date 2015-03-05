from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.debate import Debate
from apirest.models.planteamiento import Planteamiento

class PlanteamientoSobreDebate(models.Model):
    id = models.IntegerField(primary_key=True,db_column='planteamiento_sobre_debate_id')
    fk_debate = models.ForeignKey(Debate, db_column='fk_debate')
    fk_planteamiento = models.ForeignKey(Planteamiento, db_column='fk_planteamiento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().PLANTEAMIENTO_SOBRE_DEBATE
        app_label = Constants().APIREST