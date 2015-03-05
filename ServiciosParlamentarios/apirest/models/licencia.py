from __future__ import unicode_literals
from django.db import models
from apirest.models.solicitud import Solicitud
from apirest.utils.constants import Constants

class Licencia(models.Model):
    id = models.ForeignKey(Solicitud, primary_key=True, db_column='licencia_id',unique=True)
    fechadesde = models.DateTimeField(blank=True, null=True)
    fechahasta = models.DateTimeField(blank=True, null=True)
    motivo = models.TextField(blank=True)
    consueldo = models.CharField(max_length=1, blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().LICENCIA        
        app_label = Constants().APIREST