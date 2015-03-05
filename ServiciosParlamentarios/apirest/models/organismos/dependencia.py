from __future__ import unicode_literals
from django.db import models
from apirest.models.entidad import Entidad
from apirest.utils.constants import Constants

class Dependencia(models.Model):
    id = models.ForeignKey(Entidad, primary_key=True, db_column='dependencia_id',unique=True)
    nombre = models.TextField(blank=True)
    fk_dependencia = models.ForeignKey('self', db_column='fk_dependencia', blank=True, null=True)
    finicio = models.DateField(blank=True, null=True)
    ffin = models.DateField(blank=True, null=True)
    nota = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().DEPENDENCIA
        app_label = Constants().APIREST
