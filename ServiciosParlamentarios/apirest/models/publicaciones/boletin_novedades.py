from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class BoletinNovedades(models.Model):
    id = models.ForeignKey('Publicacion', primary_key=True,db_column='boletin_novedades_id')
    tipo = models.TextField()
    numero = models.SmallIntegerField(blank=True, null=True)
    fecha_hora_cierre = models.DateTimeField(blank=True, null=True, db_column='fhcierre')
    fk_camara_reunion = models.IntegerField(blank=True, null=True)
    tipo_camara = models.TextField()

    class Meta:
        managed = False
        db_table = Constants().BOLETIN_NOVEDADES