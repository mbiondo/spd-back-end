from __future__ import unicode_literals

from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.expediente import Expediente

class Firmantes(models.Model):
    expediente_id = models.ForeignKey(Expediente, db_column='expediente_id',related_name='firmantes')
    persona_fisica_id = models.IntegerField(blank=True, null=True,primary_key=True)
    cargo_persona_fisica_id = models.IntegerField(blank=True, null=True)
    cargo_tipo = models.TextField(blank=True)
    codigoexp = models.CharField(max_length=14, blank=True)
    nombre_leg_func = models.TextField(blank=True)
    tipocamara = models.TextField(blank=True)
    cargo = models.TextField(blank=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    distrito = models.TextField(blank=True)
    nombre_del_bloque = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().FIRMANTES
        app_label = Constants().APIREST
        ordering = ('orden',)