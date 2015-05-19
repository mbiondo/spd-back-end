from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.publicaciones.publicacion import Publicacion

class DiarioAsuntosEntrados(Publicacion):
    
    diario_asuntos_entrados = models.OneToOneField(Publicacion, parent_link=True)
    numero = models.SmallIntegerField()
    fecha_hora_apertura = models.DateTimeField(blank=True, null=True,db_column='fhapertura')
    fecha_hora_cierre = models.DateTimeField(blank=True, null=True,db_column='fhcierre')

    class Meta:
        managed = False
        db_table = Constants().DIARIO_ASUNTOS_ENTRADOS
