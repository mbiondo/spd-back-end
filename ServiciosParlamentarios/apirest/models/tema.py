from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class Tema(models.Model):
    id = models.IntegerField(primary_key=True,db_column='tema_id')
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = Constants().TEMA
        app_label = Constants().APIREST