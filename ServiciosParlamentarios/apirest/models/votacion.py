from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.debate import Debate

class Votacion(models.Model):
    id = models.AutoField(primary_key=True,db_column='votacion_id')
    fk_debate = models.ForeignKey(Debate, db_column='fk_debate', blank=True, null=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    sumario = models.TextField(blank=True)
    resultado = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().VOTACION
        app_label = Constants().APIREST