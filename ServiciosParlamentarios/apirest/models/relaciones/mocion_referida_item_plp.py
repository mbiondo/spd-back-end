from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.mocion import Mocion
from apirest.models.relaciones.plp_detalle_estructura import PlpDetalleEstructura

class MocionReferidaItemPlp(models.Model):
    id = models.IntegerField(primary_key=True,db_column='mocion_referida_item_plp_id')
    fk_mocion = models.ForeignKey(Mocion, db_column='fk_mocion')
    fk_plp_detalle_estructura = models.ForeignKey(PlpDetalleEstructura, db_column='fk_plp_detalle_estructura')

    class Meta:
        managed = False
        db_table = Constants().MOCION_REFERIDA_ITEM_PLP
        app_label = Constants().APIREST        