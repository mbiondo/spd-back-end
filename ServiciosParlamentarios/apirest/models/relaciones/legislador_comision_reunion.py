from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.individuos.legislador import Legislador
from apirest.models.organismos.comisiones.comision_reunion import ComisionReunion

class LegisladorComisionReunion(models.Model):
    id = models.IntegerField(primary_key=True,db_column='legislador_comision_reunion_id')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    fk_comision_reunion = models.ForeignKey(ComisionReunion, db_column='fk_comision_reunion')
    codigoasistencia = models.CharField(max_length=1)
    nota = models.TextField(blank=True)
    nivelpublicacion = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().LEGISLADOR_COMISION_REUNION
        app_label = Constants().APIREST