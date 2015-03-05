from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.expediente import Expediente
from apirest.models.tema import Tema

class TemaExpediente(models.Model):
    id = models.IntegerField(primary_key=True,db_column='tema_expediente_id')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    fk_tema = models.ForeignKey(Tema, db_column='fk_tema')

    class Meta:
        managed = False
        db_table = Constants().TEMA_EXPEDIENTE
        app_label = Constants().APIREST