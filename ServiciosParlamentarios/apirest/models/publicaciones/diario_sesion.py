from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.publicaciones.publicacion import Publicacion

class DiarioSesion(models.Model):
    id = models.ForeignKey(Publicacion, primary_key=True, db_column='diario_sesion_id',unique=True)
    fk_camara_reunion = models.IntegerField()
    fk_publicacion_estructura = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().DIARIO_SESION
        app_label = Constants().APIREST