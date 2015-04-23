from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.comisiones.comision import Comision
from apirest.models.relaciones.citacion_comision import CitacionComision

class Citacion(models.Model):
    id = models.AutoField(primary_key=True,db_column='citacion_id')
    fk_comision_cabecera = models.ForeignKey(Comision, db_column='fk_comision_cabecera', related_name='comision_cabecera')
    fecha = models.DateTimeField(blank=True, null=True)
    temario = models.TextField(blank=True)
    lugar = models.TextField(blank=True)
    visibilidad = models.IntegerField(blank=True, null=True)
    comisiones = models.ManyToManyField(Comision, through=CitacionComision, related_name='comisiones')
 
    class Meta:
        managed = False
        db_table = Constants().CITACION
        app_label = Constants().APIREST        