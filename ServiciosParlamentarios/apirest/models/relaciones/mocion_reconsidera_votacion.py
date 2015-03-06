from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.votacion import Votacion
from apirest.models.mocion import Mocion

class MocionReconsideraVotacion(models.Model):
    id = models.AutoField(primary_key=True,db_column='mocion_reconsidera_votacion_id')
    fk_votacion = models.ForeignKey(Votacion, db_column='fk_votacion')
    fk_mocion = models.ForeignKey(Mocion, db_column='fk_mocion')

    class Meta:
        managed = False
        db_table = Constants().MOCION_RECONSIDERA_VOTACION
        app_label = Constants().APIREST