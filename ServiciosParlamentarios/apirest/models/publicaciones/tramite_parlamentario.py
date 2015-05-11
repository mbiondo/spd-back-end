from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.publicaciones.publicacion import Publicacion
from apirest.models.publicaciones.boletin_asuntos_entrados import BoletinAsuntosEntrados

class TramiteParlamentario(models.Model):
    tramite_parlamentario = models.ForeignKey(Publicacion, primary_key=True)
    fk_boletin_asuntos_entrados = models.ForeignKey(BoletinAsuntosEntrados, db_column='fk_boletin_asuntos_entrados', blank=True, null=True)
    numero = models.SmallIntegerField()
    fhapertura = models.DateTimeField(blank=True, null=True)
    fhcierre = models.DateTimeField(blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = Constants().TRAMITE_PARLAMENTARIO