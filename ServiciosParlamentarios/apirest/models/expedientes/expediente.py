from __future__ import unicode_literals
from django.db import models       
from apirest.utils.constants import Constants
# from apirest.models.expedientes.expediente_origina_despacho import ExpedienteOriginaDespacho
# from apirest.models.expedientes.resultado_sobre_expediente import ResultadoSobreExpediente

class Expediente(models.Model):
    id = models.AutoField(primary_key=True,db_column='expediente_id')
    codigo_exp = models.CharField(max_length=14, blank=True,db_column='codigoexp')
    codigo_num = models.CharField(max_length=5, blank=True,db_column='codigonum') 
    codigo_origen = models.CharField(max_length=3, blank=True,db_column='codigoorigen')
    codigo_anio = models.CharField(max_length=4, blank=True,db_column='codigoanio')
    sumario = models.TextField(blank=True)
    tipo_camara = models.TextField(blank=True,db_column='tipocamara')
    tipo = models.TextField(blank=True)
    codigo_estado = models.SmallIntegerField(blank=True, null=True,db_column='codigoestado')
    fecha_caducidad = models.DateField(blank=True, null=True,db_column='fechacaducidad')
    fecha = models.DateField(blank=True, null=True)
    periodo = models.SmallIntegerField(blank=True, null=True)
    titulo = models.TextField(blank=True)
    voces = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().EXPEDIENTE
        app_label = Constants().APIREST
        ordering = ('id',)