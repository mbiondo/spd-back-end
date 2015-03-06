from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.solicitud import Solicitud
from apirest.models.expedientes.expediente import Expediente

class SolicitudReferidaExpediente(models.Model):
    id = models.AutoField(primary_key=True,db_column='solicitud_referida_expediente_id')
    fk_solicitud = models.ForeignKey(Solicitud, db_column='fk_solicitud')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    orden = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().SOLICITUD_REFERIDA_EXPEDIENTE
        app_label = Constants().APIREST        