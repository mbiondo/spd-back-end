from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.tipo_sesion_periodo import TipoSesionPeriodo
from apirest.models.organismos.camara import Camara

class Sesion(models.Model):
    id = models.IntegerField(primary_key=True,db_column='sesion_id')
    fk_tipo_sesion_periodo = models.ForeignKey(TipoSesionPeriodo, db_column='fk_tipo_sesion_periodo')
    fk_camara_cita = models.ForeignKey(Camara, db_column='fk_camara_cita', blank=True, null=True)
    fk_camara_celebra = models.ForeignKey(Camara, db_column='fk_camara_celebra', blank=True, null=True)
    tipocamara = models.TextField()
    tipo = models.TextField(blank=True)
    numero = models.SmallIntegerField(blank=True, null=True)
    nota = models.TextField(blank=True)
    benminoria = models.CharField(max_length=1, blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().SESION
        app_label = Constants().APIREST