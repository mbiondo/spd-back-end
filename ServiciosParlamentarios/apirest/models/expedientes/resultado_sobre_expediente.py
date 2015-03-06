from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.resultado import Resultado
from apirest.models.expedientes.expediente import Expediente

class ResultadoSobreExpediente(models.Model):
    id = models.AutoField(primary_key=True,db_column='resultado_sobre_expediente_id')
    fk_resultado = models.ForeignKey(Resultado, db_column='fk_resultado')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    class Meta:
        managed = False
        db_table = Constants().RESULTADO_SOBRE_EXPEDIENTE
        app_label = Constants().APIREST