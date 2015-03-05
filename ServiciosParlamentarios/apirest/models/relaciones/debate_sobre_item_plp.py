from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.debate import Debate
from apirest.models.relaciones.plp_detalle_estructura import PlpDetalleEstructura

class DebateSobreItemPlp(models.Model):
    id = models.IntegerField(primary_key=True,db_column='debate_sobre_item_plp_id')
    fk_debate = models.ForeignKey(Debate, db_column='fk_debate', unique=True)
    fk_plp_detalle_estructura = models.ForeignKey(PlpDetalleEstructura, db_column='fk_plp_detalle_estructura')

    class Meta:
        managed = False
        db_table = Constants().DEBATE_SOBRE_ITEM_PLP
        app_label = Constants().APIREST