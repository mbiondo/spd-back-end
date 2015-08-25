from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Adjunto(models.Model):
    id = models.IntegerField(primary_key=True, db_column='adjunto_id')
    entidad = models.TextField(blank=True)
    fk_entidad = models.IntegerField(blank=True, null=True)
    nombre_archivo = models.TextField(blank=True)
    extension = models.TextField(blank=True)
    url = models.TextField(blank=True)
    orden = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().ADJUNTO
        app_label = Constants().APIREST

