from __future__ import unicode_literals
from django.db import models
from apirest.models.organismos.comisiones.comision import Comision
from apirest.utils.constants import Constants
       
class ComisionHist(models.Model):
    id = models.AutoField(primary_key=True, db_column='comision_hist_id')
    fk_comision = models.ForeignKey(Comision, db_column='fk_comision', related_name='comision_hist')
    nombre = models.TextField(blank=True)
    nombre_corto = models.TextField(blank=True,db_column='nombrecorto')
    competencia = models.TextField(blank=True)
    correo = models.TextField(blank=True)
    cant_integrantes = models.SmallIntegerField(blank=True, null=True,db_column='cantintegrantes')
    fecha_desde = models.DateField(db_column='fdesde')
    fecha_hasta = models.DateField(blank=True, null=True,db_column='fhasta')
    norma_creacion = models.TextField(blank=True,db_column='normacreacion')
    norma_competencia = models.TextField(blank=True,db_column='normacompetencia')
    orden = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().COMISION_HIST
        app_label = Constants().APIREST
        
