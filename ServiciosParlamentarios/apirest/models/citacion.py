from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.relaciones.citacion_comision import CitacionComision
from apirest.models.lugar import Lugar
from apirest.models.aux_estado import AuxEstado
from apirest.models.relaciones.citacion_invita_entidad import CitacionInvitaEntidad
from apirest.models.relaciones.citacion_contiene_expediente import CitacionContieneExpediente
   
class Citacion(models.Model):
    
    id = models.AutoField(primary_key=True,db_column='citacion_id')
    fk_comision_cabecera = models.ForeignKey('Comision', db_column='fk_comision_cabecera', blank=True, null=True, related_name='comision_cabecera')
    fk_lugar = models.ForeignKey(Lugar, db_column='fk_lugar', blank=True, null=True)
    estado = models.ForeignKey(AuxEstado, db_column='fk_estado', blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    resumen = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    visibilidad = models.IntegerField(blank=True, null=True)
    reunion_conjunta = models.CharField(max_length=1, blank=True,db_column='breunionconjunta')    
    #comisiones = models.ManyToManyField('Comision', through='CitacionComision', related_name='citacion')
    citacion_comision = models.ManyToManyField(CitacionComision)
    invitados = models.ManyToManyField(CitacionInvitaEntidad, related_name='invitados')
    proyectos = models.ManyToManyField('Proyecto',through=CitacionContieneExpediente, related_name='proyectos')
    
    
    class Meta:
        managed = False
        db_table = Constants().CITACION
        app_label = Constants().APIREST        