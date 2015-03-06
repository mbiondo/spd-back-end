from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.individuos.legislador import Legislador
from apirest.models.organismos.camara_reunion import CamaraReunion

class LegisladorJuraCamaraReunion(models.Model):
    id = models.AutoField(primary_key=True,db_column='legislador_jura_camara_reunion_id')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    fk_camara_reunion = models.ForeignKey(CamaraReunion, db_column='fk_camara_reunion')

    class Meta:
        managed = False
        db_table = Constants().LEGISLADOR_JURA_CAMARA_REUNION
        app_label = Constants().APIREST