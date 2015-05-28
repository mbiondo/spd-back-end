from __future__ import unicode_literals
from django.db import models
from apirest.models.expedientes.expediente import Expediente
from apirest.models.expedientes.proyecto import Proyecto
from apirest.models.organismos.comisiones.comision import Comision
from apirest.utils.constants import Constants

class Giro(models.Model):
    id = models.AutoField(primary_key=True,db_column='giro_id')
    fk_expediente = models.ForeignKey(Proyecto, db_column='fk_expediente')#, related_name='giros')
    fk_comision = models.ForeignKey(Comision, db_column='fk_comision', related_name='comision')
    orden = models.SmallIntegerField(blank=True, null=True)
    caracter = models.TextField(blank=True)
    nota = models.TextField(blank=True)
    nro_giro = models.SmallIntegerField(db_column='nrogiro')
    fecha_vigencia = models.DateField(blank=True, null=True,db_column='fvigencia')
    fecha = models.DateField(blank=True, null=True)
    fecha_remito = models.DateField(blank=True, null=True,db_column='fremito')
    
    class Meta:
        managed = False
        db_table = Constants().GIRO
        app_label = Constants().APIREST
        ordering = ('orden',)
