from __future__ import unicode_literals

from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.proyecto import Proyecto

class Firmantes(models.Model):
    
    proyecto = models.ForeignKey(Proyecto, db_column='expediente_id',related_name='firmantes')
    id = models.IntegerField(blank=True, null=True,primary_key=True,db_column='persona_fisica_id')
    cargo_persona_fisica_id = models.IntegerField(blank=True, null=True)
    cargo_tipo = models.TextField(blank=True)
    codigo_exp = models.CharField(max_length=14, blank=True,db_column='codigoexp')
    nombre_leg_func = models.TextField(blank=True)
    tipo_camara = models.TextField(blank=True,db_column='tipocamara')
    cargo = models.TextField(blank=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    distrito = models.TextField(blank=True)
    nombre_del_bloque = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().FIRMANTES
        app_label = Constants().APIREST
        ordering = ('orden',)