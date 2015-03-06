from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.votacion import Votacion
from apirest.models.planteamiento import Planteamiento

class VotacionSobrePlanteamiento(models.Model):
    id = models.AutoField(primary_key=True,db_column='votacion_sobre_planteamiento_id')
    fk_votacion = models.ForeignKey(Votacion, db_column='fk_votacion')
    fk_planteamiento = models.ForeignKey(Planteamiento, db_column='fk_planteamiento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().VOTACION_SOBRE_PLANEAMIENTO
        app_label = Constants().APIREST