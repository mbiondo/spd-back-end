from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.expediente import Expediente

class CaducidadHist(models.Model):
    id = models.AutoField(primary_key=True,db_column='caducidad_hist_id')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    fcaducidad = models.DateTimeField(blank=True, null=True)
    observaciones = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().CADUCIDAD_HIST
        app_label = Constants().APIREST        