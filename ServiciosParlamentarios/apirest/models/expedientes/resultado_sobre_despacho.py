from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.despacho import Despacho
from apirest.models.expedientes.resultado import Resultado

class ResultadoSobreDespacho(models.Model):
    id = models.AutoField(primary_key=True,db_column='resultado_sobre_despacho_id')
    fk_despacho = models.ForeignKey(Despacho, db_column='fk_despacho')
    fk_resultado = models.ForeignKey(Resultado, db_column='fk_resultado')
    class Meta:
        managed = False
        db_table = Constants().RESULTADO_SOBRE_DESPACHO
        app_label = Constants().APIREST