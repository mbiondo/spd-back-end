from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.individuos.legislador import Legislador
from apirest.models.organismos.comisiones.comision_reunion import ComisionReunion

class LegisladorComisionReunion(models.Model):
    id = models.AutoField(primary_key=True,db_column='legislador_comision_reunion_id')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    fk_comision_reunion = models.ForeignKey(ComisionReunion, db_column='fk_comision_reunion')
    codigo_asistencia = models.CharField(max_length=1,db_column='codigoasistencia')
    nota = models.TextField(blank=True)
    nivel_publicacion = models.TextField(blank=True,db_column='nivelpublicacion')

    class Meta:
        managed = False
        db_table = Constants().LEGISLADOR_COMISION_REUNION
        app_label = Constants().APIREST