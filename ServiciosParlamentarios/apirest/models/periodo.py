from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Periodo(models.Model):
    id = models.IntegerField(primary_key=True,db_column='periodo_id')
    nroperiodo = models.SmallIntegerField(unique=True, blank=True, null=True)
    finicio = models.DateField(blank=True, null=True)
    ffin = models.DateField(blank=True, null=True)
    anioparlamentario = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().PERIODO
        app_label = Constants().APIREST