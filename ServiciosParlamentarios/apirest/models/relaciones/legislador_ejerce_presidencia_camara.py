from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.individuos.legislador import Legislador
from apirest.models.organismos.presidencia import PresidenciaCamara

class LegisladorEjercePresidenciaCamara(models.Model):
    id = models.AutoField(primary_key=True,db_column='legislador_ejerce_presidencia_camara_id')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    fk_presidencia_camara = models.ForeignKey(PresidenciaCamara, db_column='fk_presidencia_camara')
    fecha_hora_desde = models.DateTimeField(db_column='fdesde')
    fecha_hora_hasta = models.DateTimeField(db_column='fhasta')

    class Meta:
        managed = False
        db_table = Constants().LEGISLADOR_EJERCE_PRESIDENCIA_CAMARA
        app_label = Constants().APIREST