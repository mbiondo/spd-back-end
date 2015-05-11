from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Periodo(models.Model):
    id = models.AutoField(primary_key=True,db_column='periodo_id')
    nro_periodo = models.SmallIntegerField(unique=True, blank=True, null=True,db_column='nroperiodo')
    fecha_inicio = models.DateField(blank=True, null=True,db_column='finicio')
    fecha_fin = models.DateField(blank=True, null=True,db_column='ffin')
    anio_parlamentario = models.SmallIntegerField(blank=True, null=True,db_column='anioparlamentario')
    
    class Meta:
        managed = False
        db_table = Constants().PERIODO
        app_label = Constants().APIREST