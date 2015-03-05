from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.individuos.legislador import Legislador
from apirest.models.planteamiento import Planteamiento

class PlanteamientoLegislador(models.Model):
    id = models.IntegerField(primary_key=True,db_column='planteamiento_legislador_id')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    fk_planteamiento = models.ForeignKey(Planteamiento, db_column='fk_planteamiento')

    class Meta:
        managed = False
        db_table = Constants().PLANTEAMIENTO_LEGISLADOR
        app_label = Constants().APIREST        