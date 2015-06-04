from __future__ import unicode_literals
from django.db import models
from apirest.models.expedientes.expediente import Expediente
from apirest.models.organismos.despacho import Despacho
from apirest.utils.constants import Constants

class Observacion(Expediente):
    
    observacion = models.OneToOneField(Expediente, parent_link=True)
    fk_despacho = models.ForeignKey(Despacho, db_column='fk_despacho', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().OBSERVACION
        app_label = Constants().APIREST
        