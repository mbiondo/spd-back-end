from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Dictamenes(models.Model):
    dictamen_id = models.IntegerField(blank=True, null=True)
    expediente_id = models.IntegerField(blank=True, null=True)
    despacho_id = models.IntegerField(blank=True, null=True)
    codigoexp = models.CharField(max_length=14, blank=True)
    orden_dia_id = models.IntegerField(blank=True, null=True)
    tipo_dictamen = models.TextField(blank=True)
    accion_dictamen = models.TextField(blank=True)
    copete_dictamen = models.TextField(blank=True)
    bconmodificacion = models.CharField(max_length=1, blank=True)
    tipocamara = models.TextField(blank=True)
    tipo_despacho = models.TextField(blank=True)
    sumario = models.TextField(blank=True)
    art108par2 = models.CharField(max_length=1, blank=True)
    fcaducidad = models.DateField(blank=True, null=True)
    visibilidad = models.CharField(max_length=1, blank=True)
    bunanimidad = models.CharField(max_length=1, blank=True)
    tramiteespecial = models.TextField(blank=True)
    bmodificaciones = models.CharField(max_length=1, blank=True)
    textolegado = models.TextField(blank=True)
    nro_orden_dia = models.SmallIntegerField(blank=True, null=True)
    anio_orden_dia = models.SmallIntegerField(blank=True, null=True)
    fimpresion = models.DateField(blank=True, null=True)
    codigoexp_conjuntos = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().DICTAMENES
        app_label = Constants().APIREST