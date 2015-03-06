from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.camara_reunion import CamaraReunion
from apirest.models.publicaciones.diario_sesion import DiarioSesion

class VersionTaquigrafica(models.Model):
    id = models.AutoField(primary_key=True,db_column='version_taquigrafica_id')
    fk_camara_reunion = models.ForeignKey(CamaraReunion, db_column='fk_camara_reunion')
    fk_diario_sesion = models.ForeignKey(DiarioSesion, db_column='fk_diario_sesion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().VERSION_TAQUIGRAFICA
        app_label = Constants().APIREST