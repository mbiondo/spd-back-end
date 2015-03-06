from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.expediente import Expediente
from apirest.models.relaciones.plp_detalle_estructura import PlpDetalleEstructura

class ExpedienteIncluidoPlp(models.Model):
    id = models.AutoField(primary_key=True,db_column='expediente_incluido_plp_id')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente', unique=True)
    fk_plp_detalle_estructura = models.ForeignKey(PlpDetalleEstructura, db_column='fk_plp_detalle_estructura')

    class Meta:
        managed = False
        db_table = Constants().EXPEDIENTE_INLCUIDO_PLP
        app_label = Constants().APIREST