from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.citacion import Citacion
from apirest.models.organismos.comisiones.comision import Comision

class ComisionReunion(models.Model):
    id = models.AutoField(primary_key=True,db_column='comision_reunion_id')
    fk_citacion = models.ForeignKey(Citacion, db_column='fk_citacion', blank=True, null=True)
    fk_comision_cabecera = models.ForeignKey(Comision, db_column='fk_comision_cabecera')
    temario = models.TextField(blank=True)
    fecha = models.DateTimeField(blank=True, null=True)
    lugar = models.TextField(blank=True)
    art108par1 = models.CharField(max_length=1, blank=True)
    visibilidad = models.IntegerField(blank=True, null=True)
    visibilidad_parte = models.IntegerField(blank=True, null=True,db_column='visibilidadparte')
    nota = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().COMISION_REUNION
        app_label = Constants().APIREST