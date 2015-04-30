from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.citacion_gpa import CitacionGpa

class CitacionGpaGpa(models.Model):
    id = models.IntegerField(primary_key=True, db_column='citacion_gpa_gpa_id')
    fk_citacion_gpa = models.ForeignKey(CitacionGpa, db_column='fk_citacion_gpa')
    fk_grupo_parlamentario_amistad = models.ForeignKey('GrupoParlamentarioAmistad', db_column='fk_grupo_parlamentario_amistad')
    orden = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().CITACION_GPA_GPA
        app_label = Constants().APIREST           