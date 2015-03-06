from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.mocion import Mocion
from apirest.models.organismos.camara_reunion import CamaraReunion

class MocionCamaraReunion(models.Model):
    id = models.AutoField(primary_key=True,db_column='mocion_camara_reunion_id')
    fk_mocion = models.ForeignKey(Mocion, db_column='fk_mocion')
    fk_camara_reunion = models.ForeignKey(CamaraReunion, db_column='fk_camara_reunion')

    class Meta:
        managed = False
        db_table = Constants().MOCION_CAMARA_REUNION
        app_label = Constants().APIREST        