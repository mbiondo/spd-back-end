from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.tratamiento import Tratamiento
from apirest.models.organismos.comisiones.comision_reunion import ComisionReunion

class TratamientoComisionReunion(models.Model):
    id = models.IntegerField(primary_key=True,db_column='tratamiento_comision_reunion_id')
    fk_tratamiento = models.ForeignKey(Tratamiento, db_column='fk_tratamiento', unique=True)
    fk_comision_reunion = models.ForeignKey(ComisionReunion, db_column='fk_comision_reunion')

    class Meta:
        managed = False
        db_table = Constants().TRATAMIENTO_COMISION_REUNION
        app_label = Constants().APIREST