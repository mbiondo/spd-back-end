from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.bloques.bloque import Bloque
from apirest.models.individuos.legislador import Legislador

class BloqueEstructura(models.Model):
    id = models.AutoField(primary_key=True,db_column='bloque_estructura_id')
    fk_bloque = models.ForeignKey(Bloque, db_column='fk_bloque',related_name='legisladores')
    legisladores_historico = models.ForeignKey(Bloque, db_column='fk_bloque',related_name='legisladores_historico')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador',related_name='legislador')
    cargo = models.TextField(blank=True)
    cargo_muestra_como = models.TextField(blank=True, db_column='cargomuestracomo')
    jerarquia = models.SmallIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True)
    fecha_desde = models.DateTimeField(blank=True, null=True, db_column='fdesde')
    fecha_hasta = models.DateTimeField(blank=True, null=True, db_column='fhasta')
    
    class Meta:
        managed = False
        db_table = Constants().BLOQUE_ESTRUCTURA
        app_label = Constants().APIREST