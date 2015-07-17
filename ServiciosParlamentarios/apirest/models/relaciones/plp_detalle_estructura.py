from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.publicaciones.diario_sesion import DiarioSesion
from apirest.models.plp_estructura import PlpEstructura

class PlpDetalleEstructura(models.Model):
    id = models.AutoField(primary_key=True,db_column='plp_detalle_estructura_id')
    fk_plp_estructura = models.ForeignKey(PlpEstructura, db_column='fk_plp_estructura',related_name='detalle_estructura_id')
    fk_diario_sesion = models.ForeignKey(DiarioSesion, db_column='fk_diario_sesion', blank=True, null=True)
    seccion = models.TextField(blank=True)
    seccion_mostrado_como = models.TextField(blank=True)
    subseccion = models.TextField(blank=True)
    subseccion_mostrado_como = models.TextField(blank=True)
    grupo = models.TextField(blank=True)
    grupo_mostrado_como = models.TextField(blank=True)
    item = models.TextField(blank=True)
    item_sumario = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().PLP_DETALLE_ESTRUCTURA
        app_label = Constants().APIREST