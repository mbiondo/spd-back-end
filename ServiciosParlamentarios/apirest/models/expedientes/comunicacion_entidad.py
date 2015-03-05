from __future__ import unicode_literals
from django.db import models
from apirest.models.entidad import Entidad
from apirest.models.expedientes.comunicacion import Comunicacion
from apirest.utils.constants import Constants

class ComunicacionEntidad(models.Model):
    id = models.IntegerField(primary_key=True,db_column='comunicacion_entidad_id')
    fk_entidad = models.ForeignKey(Entidad, db_column='fk_entidad')
    fk_comunicacion = models.ForeignKey(Comunicacion, db_column='fk_comunicacion')
    
    class Meta:
        managed = False
        db_table = Constants().COMUNICACION_ENTIDAD
        app_label = Constants().APIREST