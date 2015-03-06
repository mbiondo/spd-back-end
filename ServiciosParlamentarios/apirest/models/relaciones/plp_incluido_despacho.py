from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.plan_labor import PlanLabor
from apirest.models.organismos.despacho import Despacho

class PlpIncluidoDespacho(models.Model):
    id = models.AutoField(primary_key=True,db_column='plp_incluido_despacho_id')
    fk_plan_labor = models.ForeignKey(PlanLabor, db_column='fk_plan_labor')
    fk_despacho = models.ForeignKey(Despacho, db_column='fk_despacho')

    class Meta:
        managed = False
        db_table = Constants().PLP_INCLUIDO_DESPACHO
        app_label = Constants().APIREST