from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.plp_estructura import PlpEstructura
from apirest.models.sesion import Sesion

class PlanLabor(models.Model):
    id = models.IntegerField(primary_key=True,db_column='plan_labor_id')
    fk_plp_estructura = models.ForeignKey(PlpEstructura, db_column='fk_plp_estructura')
    fk_sesion = models.ForeignKey(Sesion, db_column='fk_sesion', blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)
    visibilidad = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().PLAN_LABOR
        app_label = Constants().APIREST        
        