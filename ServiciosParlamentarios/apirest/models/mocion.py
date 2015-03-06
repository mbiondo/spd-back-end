from __future__ import unicode_literals
from django.db import models
from apirest.models.organismos.camara_reunion import CamaraReunion
from apirest.utils.constants import Constants

class Mocion(models.Model):
    id = models.AutoField(primary_key=True,db_column='mocion_id')
    fk_camara_reunion = models.ForeignKey(CamaraReunion, db_column='fk_camara_reunion', blank=True, null=True)
    tipo = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)
    fechahora = models.DateTimeField(blank=True, null=True)
    resultado = models.TextField(blank=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    nivel = models.SmallIntegerField(blank=True, null=True)
    dictamen = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().MOCION
        app_label = Constants().APIREST