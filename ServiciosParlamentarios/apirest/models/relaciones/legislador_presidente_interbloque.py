from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.individuos.legislador import Legislador
from apirest.models.organismos.bloques.interbloque import Interbloque

class LegisladorPresideInterbloque(models.Model):
    id = models.AutoField(primary_key=True,db_column='legislador_preside_interbloque_id')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    fk_interbloque = models.ForeignKey(Interbloque, db_column='fk_interbloque')
    fecha_inicio = models.DateField(db_column='finicio')
    fecha_fin = models.DateField(blank=True, null=True,db_column='ffin')

    class Meta:
        managed = False
        db_table = Constants().LEGISLADOR_PRESIDE_INTERBLOQUE
        app_label = Constants().APIREST