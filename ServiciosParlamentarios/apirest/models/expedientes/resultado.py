from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.debate import Debate

class Resultado(models.Model):
    id = models.AutoField(primary_key=True,db_column='resultado_id')
    fk_debate = models.ForeignKey(Debate, db_column='fk_debate', blank=True, null=True)
    resultado = models.TextField(blank=True)
    tipo = models.TextField(blank=True)
    titulo = models.TextField(blank=True)
    sumario = models.TextField(blank=True)
    texto = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().RESULTADO
        app_label = Constants().APIREST