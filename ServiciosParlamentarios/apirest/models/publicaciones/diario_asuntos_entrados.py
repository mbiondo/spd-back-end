from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class DiarioAsuntosEntrados(models.Model):
    id = models.ForeignKey('Publicacion', primary_key=True,db_column='diario_asuntos_entrados_id')
    numero = models.SmallIntegerField()
    fecha_hora_apertura = models.DateTimeField(blank=True, null=True,db_column='fhapertura')
    fecha_hora_cierre = models.DateTimeField(blank=True, null=True,db_column='fhcierre')

    class Meta:
        managed = False
        db_table = Constants().DIARIO_ASUNTOS_ENTRADOS
