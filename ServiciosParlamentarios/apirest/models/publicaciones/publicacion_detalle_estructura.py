from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.publicaciones.publicacion_estructura import PublicacionEstructura
from apirest.models.expedientes.expediente import Expediente
from apirest.models.organismos.despacho import Despacho
from apirest.models.mocion import Mocion

class PublicacionDetalleEstructura(models.Model):
    id = models.AutoField(primary_key=True,db_column='publicacion_detalle_estructura_id')
    fk_publicacion_estructura = models.ForeignKey(PublicacionEstructura, db_column='fk_publicacion_estructura')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente', blank=True, null=True)
    fk_despacho = models.ForeignKey(Despacho, db_column='fk_despacho', blank=True, null=True)
    fk_mocion = models.ForeignKey(Mocion, db_column='fk_mocion', blank=True, null=True)
    orden_item = models.SmallIntegerField(blank=True, null=True,db_column='ordenitem')
    item = models.TextField(blank=True)
    titulo_item = models.TextField(blank=True,db_column='tituloitem')
    orden_subitem = models.SmallIntegerField(blank=True, null=True,db_column='ordensubitem')
    subitem = models.TextField(blank=True)
    titulo_subitem = models.TextField(blank=True,db_column='titulosubitem')
    contador_subitem = models.SmallIntegerField(blank=True, null=True,db_column='contadorsubitem')
    
    class Meta:
        managed = False
        db_table = Constants().PUBLICACION_DETALLE_ESTRUCTURA
        app_label = Constants().APIREST