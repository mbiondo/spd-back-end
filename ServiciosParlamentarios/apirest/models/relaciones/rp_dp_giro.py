from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.rp_dp import RpDp
from apirest.models.giro import Giro

class RpDpGiro(models.Model):
    id = models.AutoField(primary_key=True,db_column='rp_dp_giro_id')
    fk_rp_dp = models.ForeignKey(RpDp, db_column='fk_rp_dp')
    fk_giro = models.ForeignKey(Giro, db_column='fk_giro')

    class Meta:
        managed = False
        db_table = Constants().RP_DP_GIRO
        app_label = Constants().APIREST