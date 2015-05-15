from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.publicaciones.publicacion import Publicacion

class BoletinAsuntosTratados(models.Model):
    
    boletin_asuntos_tratados = models.OneToOneField(Publicacion, parent_link=True)
    numero = models.SmallIntegerField(blank=True, null=True)
    fecha_hora_cierre = models.DateTimeField(blank=True, null=True,db_column='fhcierre')
    fk_camara_reunion = models.IntegerField(blank=True, null=True)
    tipo_camara = models.TextField()

    class Meta:
        managed = False
        db_table = Constants().BOLETIN_ASUNTOS_TRATADOS
