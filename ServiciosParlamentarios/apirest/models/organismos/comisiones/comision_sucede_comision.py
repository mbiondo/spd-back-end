from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.comisiones.comision import Comision

class ComisionSucedeComision(models.Model):
    id = models.IntegerField(primary_key=True,db_column='comision_sucede_comision_id')
    fk_comision = models.ForeignKey(Comision, db_column='fk_comision')
    fk_comision_sucede = models.ForeignKey(Comision, db_column='fk_comision_sucede')

    class Meta:
        managed = False
        db_table = Constants().COMISION_SUCEDE_COMISION
        app_label = Constants().APIREST        