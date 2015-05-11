from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class BoletinAsuntosTratados(models.Model):
    boletin_asuntos_tratados = models.ForeignKey('Publicacion', primary_key=True, db_column='boletin_asuntos_tratados_id')
    numero = models.SmallIntegerField(blank=True, null=True)
    fhcierre = models.DateTimeField(blank=True, null=True)
    fk_camara_reunion = models.IntegerField(blank=True, null=True)
    tipo_camara = models.TextField()

    class Meta:
        managed = False
        db_table = Constants().BOLETIN_ASUNTOS_TRATADOS
