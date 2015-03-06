from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.votacion import Votacion
from apirest.models.propuesta import Propuesta
from apirest.models.debate import Debate

class VotacionSobrePropuesta(models.Model):
    id = models.AutoField(primary_key=True,db_column='votacion_sobre_propuesta_id')
    fk_votacion = models.ForeignKey(Votacion, db_column='fk_votacion')
    fk_propuesta = models.ForeignKey(Propuesta, db_column='fk_propuesta')
    fk_debate = models.ForeignKey(Debate, db_column='fk_debate')

    class Meta:
        managed = False
        db_table = Constants().VOTACION_SOBRE_PROPUESTA
        app_label = Constants().APIREST