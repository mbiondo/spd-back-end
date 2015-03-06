from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.solicitud import Solicitud
from apirest.models.expedientes.proyecto import Proyecto

class SolicitudReproduceProyecto(models.Model):
    id = models.AutoField(primary_key=True,db_column='solicitud_reproduce_proyecto_id')
    fk_solicitud = models.ForeignKey(Solicitud, db_column='fk_solicitud')
    fk_proyecto = models.ForeignKey(Proyecto, db_column='fk_proyecto')
    orden = models.SmallIntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().SOLICITUD_REPRODUCE_PROYECTO
        app_label = Constants().APIREST