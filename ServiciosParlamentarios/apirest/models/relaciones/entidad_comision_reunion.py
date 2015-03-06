from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.entidad import Entidad
from apirest.models.organismos.comisiones.comision_reunion import ComisionReunion

class EntidadComisionReunion(models.Model):
    id = models.AutoField(primary_key=True,db_column='entidad_comision_reunion_id')
    fk_entidad = models.ForeignKey(Entidad, db_column='fk_entidad')
    fk_comision_reunion = models.ForeignKey(ComisionReunion, db_column='fk_comision_reunion')

    class Meta:
        managed = False
        db_table = Constants().ENTIDAD_COMISION_REUNION
        app_label = Constants().APIREST