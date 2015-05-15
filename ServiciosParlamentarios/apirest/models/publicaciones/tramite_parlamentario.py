from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.publicaciones.publicacion import Publicacion
from apirest.models.publicaciones.boletin_asuntos_entrados import BoletinAsuntosEntrados

class TramiteParlamentario(Publicacion):
  
    tramite_parlamentario = models.OneToOneField(Publicacion, parent_link=True)
    fk_boletin_asuntos_entrados = models.ForeignKey(BoletinAsuntosEntrados, db_column='fk_boletin_asuntos_entrados', blank=True, null=True)
    numero = models.SmallIntegerField()
    fhapertura = models.DateTimeField(blank=True, null=True)
    fecha_hora_cierre = models.DateTimeField(blank=True, null=True, db_column='fhcierre')

    class Meta:
        managed = False
        db_table = Constants().TRAMITE_PARLAMENTARIO