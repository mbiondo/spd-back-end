from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.sesion import Sesion

class CamaraReunion(models.Model):
    id = models.AutoField(primary_key=True,db_column='camara_reunion_id')
    fk_sesion = models.ForeignKey(Sesion, db_column='fk_sesion')
    finicio = models.DateTimeField(blank=True, null=True)
    ffin = models.DateTimeField(blank=True, null=True)
    nroreunion = models.SmallIntegerField(blank=True, null=True)
    bcontinuacion = models.CharField(max_length=1, blank=True)
    bpublicacion = models.CharField(max_length=1, blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().CAMARA_REUNION
        app_label = Constants().APIREST