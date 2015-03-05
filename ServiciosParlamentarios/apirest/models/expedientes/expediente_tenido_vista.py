from __future__ import unicode_literals
from django.db import models       
from apirest.models.expedientes.expediente import Expediente
from apirest.utils.constants import Constants
from apirest.models.tratamiento import Tratamiento

class ExpedienteTenidoVista(models.Model):
    id = models.IntegerField(primary_key=True,db_column='expediente_tenido_vista_id')
    fk_tratamiento = models.ForeignKey(Tratamiento, db_column='fk_tratamiento')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    class Meta:
        managed = False
        db_table = Constants().EXPEDIENTE_TENIDO_VISTA
        app_label = Constants().APIREST