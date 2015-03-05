from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.citacion import Citacion

class CitacionTemario(models.Model):
    id = models.IntegerField(primary_key=True,db_column='citacion_temario_id')
    fk_citacion = models.ForeignKey(Citacion, db_column='fk_citacion')
    orden = models.SmallIntegerField(blank=True, null=True)
    tema = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().CITACION_TEMARIO
        app_label = Constants().APIREST        