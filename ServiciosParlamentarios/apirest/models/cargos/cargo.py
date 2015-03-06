from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Cargo(models.Model):    
    id = models.AutoField(primary_key=True,db_column='cargo_id') 
    descripcion = models.TextField(blank=True)
    
    class Meta:
        managed = False
        app_label = Constants().APIREST
        db_table = Constants().CARGO
        ordering = ('id',)
