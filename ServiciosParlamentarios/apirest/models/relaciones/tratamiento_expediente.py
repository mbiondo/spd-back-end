from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.tratamiento import Tratamiento
from apirest.models.expedientes.expediente import Expediente

class TratamientoExpediente(models.Model):
    id = models.AutoField(primary_key=True,db_column='tratamiento_expediente_id')
    fk_tratamiento = models.ForeignKey(Tratamiento, db_column='fk_tratamiento')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')

    class Meta:
        managed = False
        db_table = Constants().TRATAMIENTO_EXPEDIENTE
        app_label = Constants().APIREST        