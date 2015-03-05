from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.publicaciones.publicacion import Publicacion
from apirest.models.organismos.camara_reunion import CamaraReunion
from apirest.models.publicaciones.publicacion_estructura import PublicacionEstructura

class Bae(models.Model):
    id = models.ForeignKey(Publicacion, primary_key=True, db_column='bae_id',unique=True)
    fk_publicacion_estructura = models.ForeignKey(PublicacionEstructura, db_column='fk_publicacion_estructura', blank=True, null=True)
    numero = models.SmallIntegerField(blank=True, null=True)
    fhapertura = models.DateTimeField(blank=True, null=True)
    fhcierre = models.DateTimeField(blank=True, null=True)
    fk_camara_reunion = models.ForeignKey(CamaraReunion, db_column='fk_camara_reunion', blank=True, null=True)
        
    class Meta:
        managed = False
        db_table = Constants().BAE
        app_label = Constants().APIREST