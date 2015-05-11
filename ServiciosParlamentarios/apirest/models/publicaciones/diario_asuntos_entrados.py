from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class DiarioAsuntosEntrados(models.Model):
    diario_asuntos_entrados = models.ForeignKey('Publicacion', primary_key=True,db_column='diario_asuntos_entrados_id')
    numero = models.SmallIntegerField()
    fhapertura = models.DateTimeField(blank=True, null=True)
    fhcierre = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().DIARIO_ASUNTOS_ENTRADOS
