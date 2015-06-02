from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.aux_estado import AuxEstado
from apirest.models.relaciones.citacion_gpa_gpa import CitacionGpaGpa
from apirest.models.organismos.grupo_parlamentario_amistad import GrupoParlamentarioAmistad
from apirest.models.relaciones.citacion_gpa_invita_entidad import CitacionGpaInvitaEntidad

class CitacionGpa(models.Model):
    id = models.IntegerField(primary_key=True, db_column='citacion_gpa_id')
    fecha = models.DateTimeField(blank=True, null=True)
    fk_lugar = models.ForeignKey('Lugar', db_column='fk_lugar', blank=True, null=True)
    estado = models.ForeignKey(AuxEstado, db_column='fk_estado', blank=True, null=True)
    resumen = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    visibilidad = models.IntegerField(blank=True, null=True)
    gpas = models.ManyToManyField(GrupoParlamentarioAmistad, through=CitacionGpaGpa, related_name='gpas')
    invitados_gpa = models.ManyToManyField(CitacionGpaInvitaEntidad, related_name='invitados_gpa')

    class Meta:
        managed = False
        db_table = Constants().CITACION_GPA
        app_label = Constants().APIREST        