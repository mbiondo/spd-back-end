from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.publicaciones.publicacion import Publicacion
from apirest.models.publicaciones.publicacion_estructura import PublicacionEstructura
from apirest.models.publicaciones.bae import Bae

class TpDae(models.Model):
    id = models.ForeignKey(Publicacion, primary_key=True, db_column='tp_dae_id',unique=True)
    fk_publicacion_estructura = models.ForeignKey(PublicacionEstructura, db_column='fk_publicacion_estructura', blank=True, null=True)
    fk_bae = models.ForeignKey(Bae, db_column='fk_bae', blank=True, null=True)
    numero = models.SmallIntegerField()
    fhapertura = models.DateTimeField(blank=True, null=True)
    fhcierre = models.DateTimeField(blank=True, null=True)
    tipo = models.TextField()
    
    class Meta:
        managed = False
        db_table = Constants().TP_DAE
        app_label = Constants().APIREST