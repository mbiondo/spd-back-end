from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.comisiones.comision import Comision
from apirest.models.individuos.legislador import Legislador

class ComEstructura(models.Model):
    id = models.AutoField(primary_key=True,db_column='com_estructura_id')
    fk_comision = models.ForeignKey(Comision, db_column='fk_comision', related_name='integrantes')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    cargo = models.TextField(blank=True)
    cargomuestracomo = models.TextField(blank=True)
    jerarquia = models.SmallIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)
    fdesde = models.DateTimeField(blank=True, null=True)
    fhasta = models.DateTimeField(blank=True, null=True)
    nota = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().COMISION_ESTRUCTURA
        app_label = Constants().APIREST
        
