from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.comisiones.comision import Comision
from apirest.models.organismos.comisiones.comision_reunion import ComisionReunion

class ComisionComisionReunion(models.Model):
    id = models.AutoField(primary_key=True,db_column='comision_comision_reunion_id')
    fk_comision_reunion = models.ForeignKey(ComisionReunion, db_column='fk_comision_reunion')
    fk_comision = models.ForeignKey(Comision, db_column='fk_comision')
    orden = models.SmallIntegerField(blank=True, null=True)
    nota = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().COMISION_COMISION_REUNION
        app_label = Constants().APIREST