from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.publicaciones.publicacion_detalle_estructura import PublicacionDetalleEstructura
from apirest.models.expedientes.resultado import Resultado

class ResultadoPubDetalleEstructura(models.Model):
    id = models.IntegerField(primary_key=True,db_column='resultado_pub_detalle_estructura_id')
    fk_publicacion_detalle_estructura = models.ForeignKey(PublicacionDetalleEstructura, db_column='fk_publicacion_detalle_estructura')
    fk_resultado = models.ForeignKey(Resultado, db_column='fk_resultado', blank=True, null=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    sumario = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().RESULTADO_PUB_DETALLE_ESTRUCTURA
        app_label = Constants().APIREST        
