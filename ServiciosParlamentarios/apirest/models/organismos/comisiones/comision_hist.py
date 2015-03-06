from __future__ import unicode_literals
from django.db import models
from apirest.models.organismos.comisiones.comision import Comision
from apirest.utils.constants import Constants
       
class ComisionHist(models.Model):
    id = models.AutoField(primary_key=True,db_column='comision_hist_id')
    fk_comision = models.ForeignKey(Comision, db_column='fk_comision', related_name='comision_hist')
    nombre = models.TextField(blank=True)
    nombrecorto = models.TextField(blank=True)
    competencia = models.TextField(blank=True)
    correo = models.TextField(blank=True)
    cantintegrantes = models.SmallIntegerField(blank=True, null=True)
    fdesde = models.DateField()
    fhasta = models.DateField(blank=True, null=True)
    normacreacion = models.TextField(blank=True)
    normacompetencia = models.TextField(blank=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().COMISION_HIST
        app_label = Constants().APIREST
        