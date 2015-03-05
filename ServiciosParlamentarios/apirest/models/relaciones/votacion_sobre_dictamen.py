from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.votacion import Votacion
from apirest.models.expedientes.dictamen import Dictamen
from apirest.models.debate import Debate

class VotacionSobreDictamen(models.Model):
    id = models.IntegerField(primary_key=True,db_column='votacion_sobre_dictamen_id')
    fk_votacion = models.ForeignKey(Votacion, db_column='fk_votacion')
    fk_dictamen = models.ForeignKey(Dictamen, db_column='fk_dictamen')
    fk_debate = models.ForeignKey(Debate, db_column='fk_debate')

    class Meta:
        managed = False
        db_table = Constants().VOTACION_SOBRE_DICTAMEN
        app_label = Constants().APIREST        