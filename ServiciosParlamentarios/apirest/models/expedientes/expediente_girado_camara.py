from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.camara import Camara
from apirest.models.expedientes.expediente import Expediente

class ExpedienteGiradoCamara(models.Model):
    id = models.AutoField(primary_key=True,db_column='expediente_girado_camara_id')
    fk_camara = models.ForeignKey(Camara, db_column='fk_camara')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().EXPEDIENTE_GIRADO_CAMARA
        app_label = Constants().APIREST