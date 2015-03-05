from __future__ import unicode_literals

from django.db import models
from apirest.utils.constants import Constants

class LegisladoresDetalle(models.Model):
    nombre_legislador = models.TextField(blank=True)
    finicio = models.DateField(blank=True, null=True)
    ffin = models.DateField(blank=True, null=True)
    fincorporacion = models.DateField(blank=True, null=True)
    fcese = models.DateField(blank=True, null=True)
    cargo = models.TextField(blank=True)
    distrito = models.TextField(blank=True)
    bloque = models.TextField(blank=True)
    fbloquedesde = models.DateTimeField(blank=True, null=True)
    fbloquehasta = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().LEGISLADORES_DETALLE
        app_label = Constants().APIREST  