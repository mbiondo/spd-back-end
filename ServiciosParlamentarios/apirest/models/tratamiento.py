from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.aux_tipo_tratamiento import AuxTipoTratamiento

class Tratamiento(models.Model):
    id = models.AutoField(primary_key=True,db_column='tratamiento_id')
    tipo_tratamiento = models.ForeignKey(AuxTipoTratamiento, db_column='fk_tipo_tratamiento')
    orden = models.IntegerField(blank=True, null=True)
    resumen = models.TextField(blank=True)
    fuera_de_temario = models.CharField(max_length=1, blank=True,db_column='bfueradetemario')
    sobre_tablas = models.CharField(max_length=1, blank=True,db_column='bsobretablas')
    id_parte = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().TRATAMIENTO
        app_label = Constants().APIREST