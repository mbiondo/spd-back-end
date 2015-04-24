from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class ComisionesActuales(models.Model):
    comision_id = models.IntegerField(blank=True, null=True, primary_key = True)
    nombre_comision = models.TextField(blank=True)
    nombre_corto = models.TextField(blank=True)
    correo = models.TextField(blank=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    caracter = models.CharField(max_length=1, blank=True)
    tipocamara = models.CharField(max_length=2, blank=True)
    finicio = models.DateField(blank=True, null=True)
    ffin = models.DateField(blank=True, null=True)
    sigla = models.TextField(blank=True)
    normacreacion = models.TextField(blank=True)
  
    class Meta:
        managed = False
        db_table = Constants().COMISIONES_ACTUALES
        app_label = Constants().APIREST           