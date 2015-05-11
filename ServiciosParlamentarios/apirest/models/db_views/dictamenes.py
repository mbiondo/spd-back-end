from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Dictamenes(models.Model):
    dictamen_id = models.IntegerField(blank=True, null=True)
    expediente_id = models.IntegerField(blank=True, null=True)
    despacho_id = models.IntegerField(blank=True, null=True)
    codigo_exp = models.CharField(max_length=14, blank=True,db_column='codigoexp')
    orden_dia_id = models.IntegerField(blank=True, null=True)
    tipo_dictamen = models.TextField(blank=True)
    accion_dictamen = models.TextField(blank=True)
    copete_dictamen = models.TextField(blank=True)
    con_modificacion = models.CharField(max_length=1, blank=True,db_column='bconmodificacion')
    tipo_camara = models.TextField(blank=True,db_column='tipocamara')
    tipo_despacho = models.TextField(blank=True)
    sumario = models.TextField(blank=True)
    art108par2 = models.CharField(max_length=1, blank=True)
    fecha_caducidad = models.DateField(blank=True, null=True,db_column='fcaducidad')
    visibilidad = models.CharField(max_length=1, blank=True)
    bool_unanimidad = models.CharField(max_length=1, blank=True,db_column='bunanimidad')
    tramite_especial = models.TextField(blank=True,db_column='tramiteespecial')
    modificaciones = models.CharField(max_length=1, blank=True,db_column='bmodificaciones')
    texto_legado = models.TextField(blank=True,db_column='textolegado')
    nro_orden_dia = models.SmallIntegerField(blank=True, null=True)
    anio_orden_dia = models.SmallIntegerField(blank=True, null=True)
    fecha_impresion = models.DateField(blank=True, null=True,db_column='fimpresion')
    codigo_exp_conjuntos = models.TextField(blank=True,db_column='codigoexp_conjuntos')

    class Meta:
        managed = False
        db_table = Constants().DICTAMENES
        app_label = Constants().APIREST