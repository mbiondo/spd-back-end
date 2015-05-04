from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class CitacionInvitaEntidad(models.Model):
    id = models.AutoField(primary_key=True,db_column='citacion_invita_entidad_id')
    citacion = models.ForeignKey('Citacion', db_column='fk_citacion', related_name='invitados')
    entidad = models.ForeignKey('Entidad', db_column='fk_entidad')
    nombre = models.TextField(blank=True)
    caracter = models.TextField(blank=True)
    motivo = models.TextField(blank=True)
    mail = models.TextField(blank=True)
    orden = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().CITACION_INVITA_ENTIDAD
        app_label = Constants().APIREST