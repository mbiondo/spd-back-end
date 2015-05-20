from __future__ import unicode_literals
from django.db import models
from apirest.models.organismos.despacho import Despacho
from apirest.models.publicaciones.publicacion import Publicacion
from apirest.utils.constants import Constants

class OrdenDia(Publicacion):
    
    orden_dia = models.OneToOneField(Publicacion, parent_link=True)
    despacho = models.ForeignKey(Despacho, db_column='fk_despacho', related_name='ordenes_del_dia')
    anio = models.SmallIntegerField(blank=True, null=True)
    numero = models.SmallIntegerField(blank=True, null=True)
    f113 = models.DateField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().ORDEN_DIA
        app_label = Constants().APIREST