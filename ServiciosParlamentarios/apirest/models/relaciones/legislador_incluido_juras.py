from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.individuos.legislador import Legislador
from apirest.models.relaciones.plp_detalle_estructura import PlpDetalleEstructura

class LegisladorIncluidoJuras(models.Model):
    id = models.AutoField(primary_key=True,db_column='legislador_inluido_juras_id')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    fk_plp_detalle_estructura = models.ForeignKey(PlpDetalleEstructura, db_column='fk_plp_detalle_estructura')

    class Meta:
        managed = False
        db_table = Constants().LEGISLADOR_INCLUIDO_JURAS
        app_label = Constants().APIREST