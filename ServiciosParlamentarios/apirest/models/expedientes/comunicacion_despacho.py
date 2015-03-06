from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.comunicacion import Comunicacion
from apirest.models.organismos.despacho import Despacho

class ComunicacionDespacho(models.Model):
    id = models.AutoField(primary_key=True,db_column='comunicacion_despacho_id')
    fk_comunicacion = models.ForeignKey(Comunicacion, db_column='fk_comunicacion')
    fk_despacho = models.ForeignKey(Despacho, db_column='fk_despacho', unique=True)
    norma = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().COMUNICACION_DESPACHO
        app_label = Constants().APIREST