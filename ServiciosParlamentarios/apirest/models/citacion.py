from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.comisiones.comision import Comision
from apirest.models.relaciones.citacion_comision import CitacionComision
from apirest.models.db_views.comisiones_actuales import ComisionesActuales
from apirest.models.lugar import Lugar
from apirest.models.aux_estado import AuxEstado
   
class Citacion(models.Model):
    id = models.AutoField(primary_key=True,db_column='citacion_id')
    fk_comision_cabecera = models.ForeignKey(Comision, db_column='fk_comision_cabecera', blank=True, null=True, related_name='comision_cabecera')
    fk_lugar = models.ForeignKey(Lugar, db_column='fk_lugar', blank=True, null=True)
    fk_estado = models.ForeignKey(AuxEstado, db_column='fk_estado', blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    resumen = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    visibilidad = models.IntegerField(blank=True, null=True)
    breunionconjunta = models.CharField(max_length=1, blank=True)    
    comisiones = models.ManyToManyField(ComisionesActuales, through=CitacionComision, related_name='comisiones')
 
    class Meta:
        managed = False
        db_table = Constants().CITACION
        app_label = Constants().APIREST        