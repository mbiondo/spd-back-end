from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.individuos.legislador import Legislador

class LegisladorReemplazaLegislador(models.Model):
    id = models.AutoField(primary_key=True,db_column='legislador_reemplaza_legislador_id')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    fk_legislador_reemplazado = models.ForeignKey(Legislador, db_column='fk_legislador_reemplazado')
    finicio = models.DateField(blank=True, null=True)
    ffin = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().LEGISLADOR_REEMPLAZA_LEGISLADOR
        app_label = Constants().APIREST        