from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.entidad import Entidad
from apirest.models.evento import Evento

class EntidadCelebraEvento(models.Model):
    id = models.AutoField(primary_key=True,db_column='entidad_celebra_evento_id')
    fk_entidad = models.ForeignKey(Entidad, db_column='fk_entidad')
    fk_evento = models.ForeignKey(Evento, db_column='fk_evento')

    class Meta:
        managed = False
        db_table = Constants().ENTIDAD_CELEBRA_EVENTO
        app_label = Constants().APIREST