from __future__ import unicode_literals
from django.db import models
from apirest.models.entidad import Entidad
from apirest.utils.constants import Constants
       
class Camara(models.Model):
    id = models.ForeignKey(Entidad, primary_key=True, db_column='camara_id',unique=True)
    nombre = models.TextField(blank=True)
    nota = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().CAMARA
        app_label = Constants().APIREST