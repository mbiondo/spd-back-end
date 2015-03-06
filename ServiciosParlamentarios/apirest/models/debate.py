from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.camara_reunion import CamaraReunion

class Debate(models.Model):
    id = models.AutoField(primary_key=True,db_column='debate_id')
    fk_camara_reunion = models.ForeignKey(CamaraReunion, db_column='fk_camara_reunion', blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    nivel = models.SmallIntegerField(blank=True, null=True)
    subnivel = models.SmallIntegerField(blank=True, null=True)
    letra_nivel = models.TextField(blank=True)
    letra_subnivel = models.TextField(blank=True)
    tipo = models.TextField(blank=True)
    nota = models.TextField(blank=True)
    fk_debate_padre = models.ForeignKey('self', db_column='fk_debate_padre', blank=True, null=True)
    bcontinuacion = models.CharField(max_length=1, blank=True)
    textolegado = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().DEBATE
        app_label = Constants().APIREST