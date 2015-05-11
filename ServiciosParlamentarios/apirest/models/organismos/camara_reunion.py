from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.sesion import Sesion

class CamaraReunion(models.Model):
    id = models.AutoField(primary_key=True,db_column='camara_reunion_id')
    fk_sesion = models.ForeignKey(Sesion, db_column='fk_sesion')
    fecha_inicio = models.DateTimeField(blank=True, null=True,db_column='finicio')
    fecha_fin = models.DateTimeField(blank=True, null=True,db_column='ffin')
    nro_reunion = models.SmallIntegerField(blank=True, null=True,db_column='nroreunion')
    continuacion = models.CharField(max_length=1, blank=True,db_column='bcontinuacion')
    publicacion = models.CharField(max_length=1, blank=True,db_column='bpublicacion')
    
    class Meta:
        managed = False
        db_table = Constants().CAMARA_REUNION
        app_label = Constants().APIREST