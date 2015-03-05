from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.despacho import Despacho
from apirest.models.tratamiento import Tratamiento

class TratamientoProduceDespacho(models.Model):
    id = models.IntegerField(primary_key=True,db_column='tratamiento_produce_despacho_id')
    fk_despacho = models.ForeignKey(Despacho, db_column='fk_despacho')
    fk_tratamiento = models.ForeignKey(Tratamiento, db_column='fk_tratamiento')
    
    class Meta:
        managed = False
        db_table = Constants().TRATAMIENTO_PRODUCE_DESPACHO
        app_label = Constants().APIREST