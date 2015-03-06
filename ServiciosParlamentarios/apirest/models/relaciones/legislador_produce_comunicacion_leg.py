from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.individuos.legislador import Legislador
from apirest.models.expedientes.comunicacion_leg import ComunicacionLeg

class LegisladorProduceComunicacionLeg(models.Model):
    id = models.AutoField(primary_key=True,db_column='legislador_produce_comunicacion_leg_id')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    fk_comunicacion_leg = models.ForeignKey(ComunicacionLeg, db_column='fk_comunicacion_leg')

    class Meta:
        managed = False
        db_table = Constants().LEGISLADOR_PRODUCE_COMUNICACION_LEG
        app_label = Constants().APIREST        