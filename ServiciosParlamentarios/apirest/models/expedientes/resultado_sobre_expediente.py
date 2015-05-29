from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class ResultadoSobreExpediente(models.Model):
    id = models.AutoField(primary_key=True,db_column='resultado_sobre_expediente_id')
    resultado = models.ForeignKey('Resultado', db_column='fk_resultado')
    expediente = models.ForeignKey('Proyecto', db_column='fk_expediente')
    
    class Meta:
        managed = False
        db_table = Constants().RESULTADO_SOBRE_EXPEDIENTE
        app_label = Constants().APIREST