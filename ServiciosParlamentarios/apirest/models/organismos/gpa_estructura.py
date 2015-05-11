from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class GpaEstructura(models.Model):
    id = models.IntegerField(primary_key=True, db_column='gpa_estructura_id')
    fk_grupo_parlamentario_amistad = models.ForeignKey('GrupoParlamentarioAmistad', db_column='fk_grupo_parlamentario_amistad')
    fk_legislador = models.ForeignKey('Legislador', db_column='fk_legislador')
    cargo = models.TextField(blank=True)
    cargo_muestra_como = models.TextField(blank=True,db_column='cargomuestracomo')
    jerarquia = models.SmallIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)
    fecha_desde = models.DateTimeField(blank=True, null=True,db_column='fdesde')
    fecha_hasta = models.DateTimeField(blank=True, null=True,db_column='fhasta')
    nota = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().GPA_ESTRUCTURA
        app_label = Constants().APIREST