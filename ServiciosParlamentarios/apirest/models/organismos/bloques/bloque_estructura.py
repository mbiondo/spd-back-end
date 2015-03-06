from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.bloques.bloque import Bloque
from apirest.models.individuos.legislador import Legislador

class BloqueEstructura(models.Model):
    id = models.AutoField(primary_key=True,db_column='bloque_estructura_id')
    fk_bloque = models.ForeignKey(Bloque, db_column='fk_bloque',related_name='integrantes')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador',related_name='legislador')
    cargo = models.TextField(blank=True)
    cargomuestracomo = models.TextField(blank=True)
    jerarquia = models.SmallIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)
    fdesde = models.DateTimeField(blank=True, null=True)
    fhasta = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().BLOQUE_ESTRUCTURA
        app_label = Constants().APIREST