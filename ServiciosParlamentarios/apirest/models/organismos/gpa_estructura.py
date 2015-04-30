from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class GpaEstructura(models.Model):
    id = models.IntegerField(primary_key=True, db_column='gpa_estructura_id')
    fk_grupo_parlamentario_amistad = models.ForeignKey('GrupoParlamentarioAmistad', db_column='fk_grupo_parlamentario_amistad')
    fk_legislador = models.ForeignKey('Legislador', db_column='fk_legislador')
    cargo = models.TextField(blank=True)
    cargomuestracomo = models.TextField(blank=True)
    jerarquia = models.SmallIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)
    fdesde = models.DateTimeField(blank=True, null=True)
    fhasta = models.DateTimeField(blank=True, null=True)
    nota = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().GPA_ESTRUCTURA
        app_label = Constants().APIREST