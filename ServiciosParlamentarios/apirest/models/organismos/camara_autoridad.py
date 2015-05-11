from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.camara import Camara
from apirest.models.individuos.legislador import Legislador

class CamaraAutoridad(models.Model):
    id = models.AutoField(primary_key=True,db_column='camara_autoridad_id')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    fk_camara = models.ForeignKey(Camara, db_column='fk_camara')
    cargo = models.TextField(blank=True)
    cargo_muestra_como = models.TextField(blank=True,db_column='cargomuestracomo')
    jerarquia = models.TextField(blank=True)
    estado = models.TextField(blank=True)
    fecha_desde = models.DateField(blank=True, null=True,db_column='fdesde')
    fecha_hasta = models.DateField(blank=True, null=True,db_column='fhasta')

    class Meta:
        managed = False
        db_table = Constants().CAMARA_AUTORIDAD
        app_label = Constants().APIREST
