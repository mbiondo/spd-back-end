from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.entidad import Entidad

class GrupoParlamentarioAmistad(models.Model):
    id = models.ForeignKey(Entidad, primary_key=True, db_column='grupo_parlamentario_amistad',unique=True)
    caracter = models.CharField(max_length=1, blank=True)
    tipocamara = models.CharField(max_length=2, blank=True)
    finicio = models.DateField(blank=True, null=True)
    ffin = models.DateField(blank=True, null=True)
    sigla = models.TextField(blank=True)
    normacreacion = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().GRUPO_PARLAMENTARIO_AMISTAD
        app_label = Constants().APIREST        
