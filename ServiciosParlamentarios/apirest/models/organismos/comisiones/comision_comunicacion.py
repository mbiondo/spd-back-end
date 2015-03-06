from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.comisiones.comision import Comision
from apirest.models.expedientes.comunicacion import Comunicacion

class ComisionComunicacion(models.Model):
    id = models.AutoField(primary_key=True,db_column='comision_comunicacion_id')
    fk_comision = models.ForeignKey(Comision, db_column='fk_comision')
    fk_comunicacion = models.ForeignKey(Comunicacion, db_column='fk_comunicacion')

    class Meta:
        managed = False
        db_table = Constants().COMISION_COMUNICACION
        app_label = Constants().APIREST