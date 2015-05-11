from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.relaciones.plp_detalle_estructura import PlpDetalleEstructura
from apirest.models.publicaciones.boletin_asuntos_entrados import BoletinAsuntosEntrados

class PlpDetalleEstructuraIncluyeBae(models.Model):
    id = models.AutoField(primary_key=True,db_column='plp_detalle_estructura_incluye_bae_id')
    fk_plp_detalle_estructura = models.ForeignKey(PlpDetalleEstructura, db_column='fk_plp_detalle_estructura')
    fk_bae = models.ForeignKey(BoletinAsuntosEntrados, db_column='fk_bae')

    class Meta:
        managed = False
        db_table = Constants().PLP_DETALLE_ESTRUCTURA_INCLUYE_BAE
        app_label = Constants().APIREST        