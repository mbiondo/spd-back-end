from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class ComisionesDetalle(models.Model):
    nombre_comision = models.TextField(blank=True, primary_key = True)
    nombre_corto = models.TextField(blank=True)
    comision_id = models.IntegerField(blank=True, null=True)
    caracter = models.CharField(max_length=1, blank=True)
    tipo_camara = models.CharField(max_length=2, blank=True,db_column='tipocamara')
    fecha_inicio = models.DateField(blank=True, null=True,db_column='finicio')
    fecha_fin = models.DateField(blank=True, null=True,db_column='ffin')
    sigla = models.TextField(blank=True)
    norma_creacion = models.TextField(blank=True,db_column='normacreacion')
    nombre_legislador = models.TextField(blank=True)
    cargo = models.TextField(blank=True)
    estado = models.CharField(max_length=1, blank=True)
    fecha_desde = models.DateTimeField(blank=True, null=True,db_column='fdesde')
    fecha_hasta = models.DateTimeField(blank=True, null=True,db_column='fhasta')
    
    class Meta:
        managed = False
        db_table = Constants().COMISIONES_DETALLE
        app_label = Constants().APIREST                      