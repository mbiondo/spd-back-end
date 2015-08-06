from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.comisiones.comision_reunion import ComisionReunion

class Debate(models.Model):
    id = models.AutoField(primary_key=True,db_column='debate_id')
    fk_camara_reunion = models.ForeignKey(ComisionReunion, db_column='fk_camara_reunion',related_name='debate_comision_reunion')
    fecha = models.DateTimeField(blank=True, null=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    nivel = models.SmallIntegerField(blank=True, null=True)
    subnivel = models.SmallIntegerField(blank=True, null=True)
    letra_nivel = models.TextField(blank=True)
    letra_subnivel = models.TextField(blank=True)
    tipo = models.TextField(blank=True)
    nota = models.TextField(blank=True)
    fk_debate_padre = models.ForeignKey('self', db_column='fk_debate_padre', blank=True, null=True)
    continuacion = models.CharField(max_length=1, blank=True,db_column='bcontinuacion')
    texto_legado = models.TextField(blank=True,db_column='textolegado')
    
    class Meta:
        managed = False
        db_table = Constants().DEBATE
        app_label = Constants().APIREST