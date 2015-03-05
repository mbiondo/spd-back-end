from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.bloques.bloque import Bloque
from apirest.models.organismos.bloques.interbloque import Interbloque

class BlqInterblq(models.Model):
    id = models.IntegerField(primary_key=True,db_column='blq_interblq_id')
    fk_bloque = models.ForeignKey(Bloque, db_column='fk_bloque')
    fk_interbloque = models.ForeignKey(Interbloque, db_column='fk_interbloque')
    finicio = models.DateField(blank=True, null=True)
    ffin = models.DateField(blank=True, null=True)
    caracter = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().BLQ_INTERBLOQUE
        app_label = Constants().APIREST