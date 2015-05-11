from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.tipo_sesion_periodo import TipoSesionPeriodo
from apirest.models.organismos.camara import Camara

class Sesion(models.Model):
    id = models.AutoField(primary_key=True,db_column='sesion_id')
    fk_tipo_sesion_periodo = models.ForeignKey(TipoSesionPeriodo, db_column='fk_tipo_sesion_periodo')
    fk_camara_cita = models.ForeignKey(Camara, db_column='fk_camara_cita', blank=True, null=True)
    fk_camara_celebra = models.ForeignKey(Camara, db_column='fk_camara_celebra', blank=True, null=True)
    tipo_camara = models.TextField(db_column='tipocamara')
    tipo = models.TextField(blank=True)
    numero = models.SmallIntegerField(blank=True, null=True)
    nota = models.TextField(blank=True)
    en_minoria = models.CharField(max_length=1, blank=True,db_column='benminoria')
    
    class Meta:
        managed = False
        db_table = Constants().SESION
        app_label = Constants().APIREST