from __future__ import unicode_literals
from django.db import models       
from apirest.models.expedientes.expediente import Expediente
from apirest.models.organismos.despacho import Despacho
from apirest.utils.constants import Constants

class ExpedienteOriginaDespacho(models.Model):
    id = models.AutoField(primary_key=True,db_column='expediente_origina_despacho_id')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    fk_despacho = models.ForeignKey(Despacho, db_column='fk_despacho')
    orden = models.IntegerField(blank=True, null=True)
    solo_vista = models.CharField(max_length=1, blank=True,db_column='bsolovista')
    
    class Meta:
        managed = False
        db_table = Constants().EXPEDIENTE_ORIGINA_DESPACHO
        app_label = Constants().APIREST