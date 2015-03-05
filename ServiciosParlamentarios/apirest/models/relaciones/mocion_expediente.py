from __future__ import unicode_literals
from django.db import models
from apirest.models.mocion import Mocion
from apirest.models.expedientes.expediente import Expediente
from apirest.utils.constants import Constants

class MocionExpediente(models.Model):
    id = models.IntegerField(primary_key=True,db_column='mocion_expediente_id')
    fk_mocion = models.ForeignKey(Mocion, db_column='fk_mocion')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    orden = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().MOCION_EXPEDIENTE
        app_label = Constants().APIREST