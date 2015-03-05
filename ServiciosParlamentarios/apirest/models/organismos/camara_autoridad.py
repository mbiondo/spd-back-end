from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.organismos.camara import Camara
from apirest.models.individuos.legislador import Legislador

class CamaraAutoridad(models.Model):
    id = models.IntegerField(primary_key=True,db_column='camara_autoridad_id')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    fk_camara = models.ForeignKey(Camara, db_column='fk_camara')
    cargo = models.TextField(blank=True)
    cargomuestracomo = models.TextField(blank=True)
    jerarquia = models.TextField(blank=True)
    estado = models.TextField(blank=True)
    fdesde = models.DateField(blank=True, null=True)
    fhasta = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().CAMARA_AUTORIDAD
        app_label = Constants().APIREST
