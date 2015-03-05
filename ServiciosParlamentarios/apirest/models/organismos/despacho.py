from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Despacho(models.Model):
    id = models.IntegerField(primary_key=True,db_column='despacho_id')
    numero = models.SmallIntegerField(blank=True, null=True)
    anio = models.SmallIntegerField(blank=True, null=True)
    tipocamara = models.TextField(blank=True)
    sumario = models.TextField(blank=True)
    art108par2 = models.CharField(max_length=1, blank=True)
    tipo = models.TextField(blank=True)
    fcaducidad = models.DateField(blank=True, null=True)
    visibilidad = models.CharField(max_length=1, blank=True)
    bunanimidad = models.CharField(max_length=1, blank=True)
    tramiteespecial = models.TextField(blank=True)
    bmodificaciones = models.CharField(max_length=1, blank=True)
    textolegado = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().DESPACHO
        app_label = Constants().APIREST