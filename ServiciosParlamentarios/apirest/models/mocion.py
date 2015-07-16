from __future__ import unicode_literals
from django.db import models
from apirest.models.organismos.camara_reunion import CamaraReunion
from apirest.utils.constants import Constants

class Mocion(models.Model):
    id = models.AutoField(primary_key=True,db_column='mocion_id')
    fk_camara_reunion = models.ForeignKey(CamaraReunion, db_column='fk_camara_reunion', blank=True, null=True)
    tipo = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)
    fecha_hora = models.DateTimeField(blank=True, null=True,db_column='fechahora')
    resultado = models.TextField(blank=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    nivel = models.SmallIntegerField(blank=True, null=True)
    dictamen = models.TextField(blank=True)
    fk_plan_labor = models.ForeignKey('PlanLabor', db_column='fk_plan_labor', blank=True, null=True)
        
    class Meta:
        managed = False
        db_table = Constants().MOCION
        app_label = Constants().APIREST