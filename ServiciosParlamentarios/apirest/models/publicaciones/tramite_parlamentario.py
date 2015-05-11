from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.publicaciones.publicacion import Publicacion
from apirest.models.publicaciones.boletin_asuntos_entrados import BoletinAsuntosEntrados

class TramiteParlamentario(models.Model):
    id = models.ForeignKey(Publicacion, primary_key=True,db_column='tramite_parlamentario_id' )
    fk_boletin_asuntos_entrados = models.ForeignKey(BoletinAsuntosEntrados, db_column='fk_boletin_asuntos_entrados', blank=True, null=True)
    numero = models.SmallIntegerField()
    fecha_hora_apertura = models.DateTimeField(blank=True, null=True,db_column='fhapertura')
    fecha_hora_cierre = models.DateTimeField(blank=True, null=True,db_column='fhcierre')
    

    class Meta:
        managed = False
        db_table = Constants().TRAMITE_PARLAMENTARIO