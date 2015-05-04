from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
# from apirest.models.citacion import Citacion
from apirest.models.entidad import Entidad

class CitacionInvitaEntidad(models.Model):
    id = models.AutoField(primary_key=True,db_column='citacion_invita_entidad_id')
    fk_citacion = models.ForeignKey('Citacion', db_column='fk_citacion')
    fk_entidad = models.ForeignKey(Entidad, db_column='fk_entidad')

    class Meta:
        managed = False
        db_table = Constants().CITACION_INVITA_ENTIDAD
        app_label = Constants().APIREST