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
    tipo_camara = models.CharField(max_length=2, blank=True,db_column='tipocamara')
    fecha_inicio = models.DateField(blank=True, null=True,db_column='finicio')
    fecha_fin = models.DateField(blank=True, null=True,db_column='ffin')
    sigla = models.TextField(blank=True)
    norma_creacion = models.TextField(blank=True,db_column='normacreacion')
  
    class Meta:
        managed = False
        db_table = Constants().COMISIONES_ACTUALES
        app_label = Constants().APIREST           