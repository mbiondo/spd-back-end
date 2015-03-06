from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.individuos.legislador import Legislador
from apirest.models.organismos.camara_reunion import CamaraReunion

class LegisladorCamaraReunion(models.Model):
    id = models.AutoField(primary_key=True,db_column='legislador_camara_reunion_id')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    fk_camara_reunion = models.ForeignKey(CamaraReunion, db_column='fk_camara_reunion')
    codigoasistencia = models.CharField(max_length=1)
    nota = models.TextField(blank=True)
    nivelpublicacion = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().LEGISLADOR_CAMARA_REUNION
        app_label = Constants().APIREST