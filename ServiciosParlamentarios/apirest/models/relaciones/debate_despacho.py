from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.debate import Debate
from apirest.models.organismos.despacho import Despacho

class DebateDespacho(models.Model):
    id = models.AutoField(primary_key=True,db_column='debate_despacho_id')
    fk_despacho = models.ForeignKey(Despacho, db_column='fk_despacho')
    fk_debate = models.ForeignKey(Debate, db_column='fk_debate')
    tipo_consideracion = models.TextField(blank=True,db_column='tipoconsideracion')
    comunicacion = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().DEBATE_DESPACHO
        app_label = Constants().APIREST