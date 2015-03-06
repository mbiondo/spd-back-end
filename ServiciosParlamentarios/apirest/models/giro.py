from __future__ import unicode_literals
from django.db import models
from apirest.models.expedientes.expediente import Expediente
from apirest.models.organismos.comisiones.comision import Comision
from apirest.utils.constants import Constants

class Giro(models.Model):
    id = models.AutoField(primary_key=True,db_column='giro_id')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente', related_name='giros')
    fk_comision = models.ForeignKey(Comision, db_column='fk_comision', related_name='comision')
    orden = models.SmallIntegerField(blank=True, null=True)
    caracter = models.TextField(blank=True)
    nota = models.TextField(blank=True)
    nrogiro = models.SmallIntegerField()
    fvigencia = models.DateField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    fremito = models.DateField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().GIRO
        app_label = Constants().APIREST
        ordering = ('orden',)
