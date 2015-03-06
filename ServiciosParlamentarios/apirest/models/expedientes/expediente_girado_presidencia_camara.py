from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.expediente import Expediente
from apirest.models.organismos.presidencia import PresidenciaCamara

class ExpedienteGiradoPresidenciaCamara(models.Model):
    id = models.AutoField(primary_key=True,db_column='expediente_girado_presidencia_camara_id')
    fk_presidencia_camara = models.ForeignKey(PresidenciaCamara, db_column='fk_presidencia_camara')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = Constants().EXPEDIENTE_GIRADO_PRESIDENCIA_CAMARA
        app_label = Constants().APIREST