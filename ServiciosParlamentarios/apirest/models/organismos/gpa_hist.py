from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class GpaHist(models.Model):
    id = models.IntegerField(primary_key=True, db_column='gpa_hist_id')
    fk_grupo_parlamentario_amistad = models.ForeignKey('GrupoParlamentarioAmistad', db_column='fk_grupo_parlamentario_amistad')
    nombre = models.TextField(blank=True)
    nombrecorto = models.TextField(blank=True)
    competencia = models.TextField(blank=True)
    correo = models.TextField(blank=True)
    cantintegrantes = models.SmallIntegerField(blank=True, null=True)
    fdesde = models.DateField()
    fhasta = models.DateField(blank=True, null=True)
    normacreacion = models.TextField(blank=True)
    normacompetencia = models.TextField(blank=True)
    orden = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().GPA_HIST
        app_label = Constants().APIREST        