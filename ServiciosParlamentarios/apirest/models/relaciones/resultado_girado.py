from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.giro import Giro
from apirest.models.expedientes.resultado import Resultado

class ResultadoGirado(models.Model):
    id = models.AutoField(primary_key=True,db_column='resultado_girado_id')
    fk_giro = models.ForeignKey(Giro, db_column='fk_giro', unique=True)
    fk_resultado = models.ForeignKey(Resultado, db_column='fk_resultado')

    class Meta:
        managed = False
        db_table = Constants().RESULTADO_GIRADO
        app_label = Constants().APIREST        