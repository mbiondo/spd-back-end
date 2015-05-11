from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.dictamen import Dictamen

class Propuesta(models.Model):
    id = models.AutoField(primary_key=True,db_column='propuesta_id')
    fk_dictamen = models.ForeignKey(Dictamen, db_column='fk_dictamen')
    nro_orden = models.TextField(blank=True,db_column='nroorden')
    tipo = models.TextField(blank=True)
    sumario = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants.PROPUESTA
        app_label = Constants().APIREST