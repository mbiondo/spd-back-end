from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
                
class BloqueDetalle(models.Model):
    bloque_id = models.IntegerField(blank=True, null=True, primary_key = True)
    nombre = models.TextField(blank=True)
    nro_integrantes = models.SmallIntegerField(blank=True, null=True, db_column='nrointegrantes')
    fecha_inicio = models.DateField(blank=True, null=True,db_column='finicio')
    fecha_fin = models.DateField(blank=True, null=True,db_column='ffin')
    tipo_camara = models.CharField(max_length=1, blank=True,db_column='tipocamara')
    nota = models.TextField(blank=True)
    sigla = models.TextField(blank=True)
    nombre_legislador = models.TextField(blank=True)
    cargo = models.TextField(blank=True)
    jerarquia = models.SmallIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)
    fecha_desde = models.DateTimeField(blank=True, null=True,db_column='fdesde')
    fecha_hasta = models.DateTimeField(blank=True, null=True,db_column='fhasta')
    cargo_legislador = models.TextField(blank=True)
    partido = models.TextField(blank=True)
    fecha_inicio_legislador = models.DateField(blank=True, null=True,db_column='finicio_legislador')
    fecha_fin_legislador = models.DateField(blank=True, null=True,db_column='ffin_legislador')
    
    class Meta:
        managed = False
        db_table = Constants().BLOQUE_DETALLE
        app_label = Constants().APIREST      