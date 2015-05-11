from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Despacho(models.Model):
    id = models.AutoField(primary_key=True,db_column='despacho_id')
    numero = models.SmallIntegerField(blank=True, null=True)
    anio = models.SmallIntegerField(blank=True, null=True)
    tipo_camara = models.TextField(blank=True,db_column='tipocamara')
    sumario = models.TextField(blank=True)
    art108par2 = models.CharField(max_length=1, blank=True)
    tipo = models.TextField(blank=True)
    fecha_caducidad = models.DateField(blank=True, null=True,db_column='fcaducidad')
    visibilidad = models.CharField(max_length=1, blank=True)
    unanimidad = models.CharField(max_length=1, blank=True,db_column='bunanimidad')
    tramite_especial = models.TextField(blank=True,db_column='tramiteespecial')
    modificaciones = models.CharField(max_length=1, blank=True,db_column='bmodificaciones')
    texto_legado = models.TextField(blank=True,db_column='textolegado')
    
    class Meta:
        managed = False
        db_table = Constants().DESPACHO
        app_label = Constants().APIREST