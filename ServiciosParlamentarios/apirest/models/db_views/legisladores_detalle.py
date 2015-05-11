from __future__ import unicode_literals

from django.db import models
from apirest.utils.constants import Constants

class LegisladoresDetalle(models.Model):
    nombre_legislador = models.TextField(blank=True)
    fecha_inicio = models.DateField(blank=True, null=True,db_column='finicio')
    fecha_fin = models.DateField(blank=True, null=True,db_column='ffin')
    fecha_incorporacion = models.DateField(blank=True, null=True,db_column='fincorporacion')
    fecha_cese = models.DateField(blank=True, null=True,db_column='fcese')
    cargo = models.TextField(blank=True)
    distrito = models.TextField(blank=True)
    bloque = models.TextField(blank=True)
    fecha_bloque_desde = models.DateTimeField(blank=True, null=True,db_column='fbloquedesde')
    fecha_bloque_hasta = models.DateTimeField(blank=True, null=True,db_column='fbloquehasta')
    
    class Meta:
        managed = False
        db_table = Constants().LEGISLADORES_DETALLE
        app_label = Constants().APIREST  