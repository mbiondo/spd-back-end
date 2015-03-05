from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.norma import Norma
from apirest.models.sancion import Sancion

class Veto(models.Model):
    id = models.IntegerField(primary_key=True,db_column='veto_id')
    fk_norma = models.ForeignKey(Norma, db_column='fk_norma')
    fk_sancion = models.ForeignKey(Sancion, db_column='fk_sancion', blank=True, null=True)
    estotal = models.CharField(max_length=1, blank=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().VETO
        app_label = Constants().APIREST