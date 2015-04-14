from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class CitacionComision(models.Model):
    id = models.AutoField(primary_key=True,db_column='citacion_comision_id')
    fk_citacion = models.ForeignKey('apirest.models.citacion.Citacion',db_column='fk_citacion')
    fk_comision = models.ForeignKey('apirest.models.organismos.comisiones.comision.Comision',db_column='fk_comision')
    orden = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().CITACION_COMISION
        app_label = Constants().APIREST        
