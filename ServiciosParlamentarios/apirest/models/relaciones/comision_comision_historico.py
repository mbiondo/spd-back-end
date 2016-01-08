from __future__ import unicode_literals
from django.db import models
from apirest.models.organismos.comisiones.comision import Comision
from apirest.models.organismos.comisiones.comision_hist import ComisionHist
from apirest.utils.constants import Constants


class ComisionComisionHist(models.Model):
    id = models.IntegerField(primary_key=True,db_column='comision_comision_hist_id')
    comision_hist = models.ForeignKey(ComisionHist, db_column='fk_comision_hist')
    fk_comision = models.ForeignKey(Comision, db_column='fk_comision', related_name='comision_comision_hist')

    class Meta:
        managed = False
        db_table = Constants().COMISION_COMISION_HIST
        app_label = Constants().APIREST        
