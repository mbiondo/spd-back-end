from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.camara import Camara
from apirest.models.organismos.despacho import Despacho

class CamaraProduceDespacho(models.Model):
    id = models.AutoField(primary_key=True,db_column='camara_produce_despacho_id')
    fk_camara = models.ForeignKey(Camara, db_column='fk_camara')
    fk_despacho = models.ForeignKey(Despacho, db_column='fk_despacho')
    fk_camara_reunion = models.IntegerField()

    class Meta:
        managed = False
        db_table = Constants().CAMARA_PRODUCE_DESPACHO
        app_label = Constants().APIREST        