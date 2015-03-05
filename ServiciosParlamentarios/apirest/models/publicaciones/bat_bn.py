from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.publicaciones.publicacion import Publicacion
from apirest.models.publicaciones.publicacion_estructura import PublicacionEstructura

class BatBn(models.Model):
    id = models.ForeignKey(Publicacion, primary_key=True, db_column='bat_bn_id',unique=True)
    tipo = models.TextField()
    fk_publicacion_estructura = models.ForeignKey(PublicacionEstructura, db_column='fk_publicacion_estructura')
    numero = models.SmallIntegerField(blank=True, null=True)
    fhcierre = models.DateTimeField(blank=True, null=True)
    fk_camara_reunion = models.IntegerField(blank=True, null=True)
    tipo_camara = models.TextField()
    
    class Meta:
        managed = False
        db_table = Constants().BAE_BN
        app_label = Constants().APIREST