from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Lugar(models.Model):
    id = models.IntegerField(primary_key=True, db_column='lugar_id')
    nombre = models.TextField(blank=True)
    direccion = models.TextField(blank=True)
    ubicacion = models.TextField(blank=True)
    piso = models.TextField(blank=True)
    oficina = models.TextField(blank=True)
    telefono = models.TextField(blank=True)
    interno = models.TextField(blank=True)
    capacidadmax = models.SmallIntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().LUGAR        
        app_label = Constants().APIREST