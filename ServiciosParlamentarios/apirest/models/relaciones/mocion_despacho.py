from __future__ import unicode_literals
from django.db import models
from apirest.models.mocion import Mocion
from apirest.models.organismos.despacho import Despacho
from apirest.utils.constants import Constants

class MocionSobreDespacho(models.Model):
    id = models.IntegerField(primary_key=True,db_column='mocion_sobre_despacho_id')
    fk_despacho = models.ForeignKey(Despacho, db_column='fk_despacho')
    fk_mocion = models.ForeignKey(Mocion, db_column='fk_mocion')
    
    class Meta:
        managed = False
        db_table = Constants().MOCION_SOBRE_DESPACHO
        app_label = Constants().APIREST