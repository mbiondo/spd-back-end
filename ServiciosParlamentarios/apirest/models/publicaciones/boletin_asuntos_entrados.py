from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.publicaciones.publicacion import Publicacion

class BoletinAsuntosEntrados(Publicacion):
    
    boletin_asuntos_entrados = models.OneToOneField(Publicacion, parent_link=True)
    numero = models.SmallIntegerField(blank=True, null=True)
    fecha_hora_apertura = models.DateTimeField(blank=True, null=True,db_column='fhapertura')
    fecha_hora_cierre = models.DateTimeField(blank=True, null=True,db_column='fhcierre')
    fk_camara_reunion = models.ForeignKey('CamaraReunion', db_column='fk_camara_reunion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().BOLETIN_ASUNTOS_ENTRADOS
