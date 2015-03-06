from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.entidad import Entidad
from apirest.models.relaciones.evento_reunion import EventoReunion

class EntidadParticipaEventoReunion(models.Model):
    id = models.AutoField(primary_key=True,db_column='entidad_participa_evento_reunion_id')
    fk_entidad = models.ForeignKey(Entidad, db_column='fk_entidad')
    fk_evento_reunion = models.ForeignKey(EventoReunion, db_column='fk_evento_reunion')
    participacion = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().ENTIDAD_PARTICIPA_EVENTO_REUNION
        app_label = Constants().APIREST