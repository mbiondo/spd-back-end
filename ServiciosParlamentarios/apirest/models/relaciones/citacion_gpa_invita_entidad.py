from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.citacion_gpa import CitacionGpa

class CitacionGpaInvitaEntidad(models.Model):
    id = models.IntegerField(primary_key=True,db_column='citacion_gpa_invita_entidad_id')
    fk_citacion_gpa = models.ForeignKey(CitacionGpa, db_column='fk_citacion_gpa', blank=True, null=True)
    fk_entidad = models.ForeignKey('Entidad', db_column='fk_entidad', blank=True, null=True)
    nombre = models.TextField(blank=True)
    caracter = models.TextField(blank=True)
    motivo = models.TextField(blank=True)
    mail = models.TextField(blank=True)
    orden = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().CITACION_GPA_INVITA_ENTIDAD
        app_label = Constants().APIREST