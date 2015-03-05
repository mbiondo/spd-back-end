from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.individuos.legislador import Legislador
from apirest.models.votacion import Votacion

class LegisladorVotacion(models.Model):
    id = models.IntegerField(primary_key=True,db_column='legislador_votacion_id')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    fk_votacion = models.ForeignKey(Votacion, db_column='fk_votacion')
    sentido = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().LEGISLADOR_VOTACION
        app_label = Constants().APIREST