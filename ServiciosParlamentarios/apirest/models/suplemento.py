from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.observacion import Observacion
from apirest.models.publicaciones.orden_dia import OrdenDia

class Suplemento(models.Model):
    id = models.AutoField(primary_key=True,db_column='suplemento_id')
    orden = models.SmallIntegerField()
    sumario = models.TextField()
    fk_observacion = models.ForeignKey(Observacion, db_column='fk_observacion')
    fk_orden_dia = models.ForeignKey(OrdenDia, db_column='fk_orden_dia')
    
    class Meta:
        managed = False
        db_table = Constants().SUPLEMENTO
        app_label = Constants().APIREST