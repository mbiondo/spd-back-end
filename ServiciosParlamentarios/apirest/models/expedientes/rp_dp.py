from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.expediente import Expediente

class RpDp(models.Model):
    id = models.ForeignKey(Expediente, primary_key=True, db_columns='rp_dp_id', unique=True)
    
    class Meta:
        managed = False
        db_table = Constants().RP_DP
        app_label = Constants().APIREST
