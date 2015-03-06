from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.mocion import Mocion
from apirest.models.individuos.legislador import Legislador

class LegisladorRealizaMocion(models.Model):
    id = models.AutoField(primary_key=True,db_column='legislador_realiza_mocion_id')
    fk_mocion = models.ForeignKey(Mocion, db_column='fk_mocion')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')

    class Meta:
        managed = False
        db_table = Constants().LEGISLADOR_REALIZA_MOCION
        app_label = Constants().APIREST        