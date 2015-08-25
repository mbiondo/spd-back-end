from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class ComisionComisionHist(models.Model):
    id = models.IntegerField(primary_key=True,db_column='comision_comision_hist_id')
    fk_comision_hist = models.IntegerField()
    fk_comision = models.IntegerField()

    class Meta:
        managed = False
        db_table = Constants().COMISION_COMISION_HIST
        app_label = Constants().APIREST        
