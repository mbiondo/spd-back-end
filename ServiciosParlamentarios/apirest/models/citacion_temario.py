from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class CitacionTemario(models.Model):
    id = models.AutoField(primary_key=True,db_column='citacion_temario_id')
    fk_citacion = models.ForeignKey('Citacion', db_column='fk_citacion',related_name='temario')
    orden = models.SmallIntegerField(blank=True, null=True)
    tema = models.TextField(blank=True)
    art_109 = models.CharField(max_length=1, blank=True, db_column='bart109')
    sobre_trablas = models.CharField(max_length=1, blank=True, db_column='bsobretrablas')
    exp_agrupados = models.CharField(max_length=1, blank=True, db_column='bexpagrupados')

    class Meta:
        managed = False
        db_table = Constants().CITACION_TEMARIO
        app_label = Constants().APIREST
                