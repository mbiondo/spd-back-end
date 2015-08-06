from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.citacion_temario import CitacionTemario

class CitacionContieneExpediente(models.Model):
    id = models.AutoField(primary_key=True,db_column='citacion_contiene_expediente_id')
    fk_expediente = models.ForeignKey('Expediente', db_column='fk_expediente', blank=True, null=True)
    fk_citacion = models.ForeignKey('Citacion', db_column='fk_citacion', blank=True, null=True)
    fk_citacion_temario = models.ForeignKey(CitacionTemario, db_column='fk_citacion_temario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().CITACION_CONTIENE_EXPEDIENTE
        app_label = Constants().APIREST        