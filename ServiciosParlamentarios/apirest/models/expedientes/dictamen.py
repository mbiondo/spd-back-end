from __future__ import unicode_literals
from django.db import models
from apirest.models.organismos.despacho import Despacho
from apirest.utils.constants import Constants

class Dictamen(models.Model):
    id = models.AutoField(primary_key=True,db_column='dictamen_id')
    fk_despacho = models.ForeignKey(Despacho, db_column='fk_despacho')
    tipo = models.TextField(blank=True)
    copete = models.TextField(blank=True)
    accion = models.TextField(blank=True)
    bconmodificacion = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = Constants().DICTAMEN
        app_label = Constants().APIREST