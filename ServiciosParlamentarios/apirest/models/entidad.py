from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Entidad(models.Model):    
    id = models.AutoField(primary_key=True,db_column='entidad_id')
    selector = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=40, blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().ENTIDAD
        app_label = Constants().APIREST
