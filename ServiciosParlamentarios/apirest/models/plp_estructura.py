from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class PlpEstructura(models.Model):
    
    id = models.AutoField(primary_key=True,db_column='plp_estructura_id')
    descripcion = models.TextField()
    fecha_desde = models.DateField(db_column='fdesde')
    fecha_hasta = models.DateField(blank=True, null=True,db_column='fhasta')    

    class Meta:
        managed = False
        db_table = Constants().PLP_ESTRUCTURA
        app_label = Constants().APIREST