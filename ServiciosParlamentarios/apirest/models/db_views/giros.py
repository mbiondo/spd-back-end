from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.proyecto import Proyecto

class Giros(models.Model):
    proyecto = models.ForeignKey(Proyecto, db_column='expediente_id',related_name='giros')
    comision_id = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True, primary_key=True, db_column='giro_id')
    codigo_exp = models.CharField(max_length=14, blank=True,db_column='codigoexp')
    comision_nombre = models.TextField(blank=True)
    comision_nombre_corto = models.TextField(blank=True)
    camara = models.CharField(max_length=2, blank=True)
    order_giro = models.SmallIntegerField(blank=True, null=True)
    nro_giro = models.SmallIntegerField(blank=True, null=True)
    fecha_giro = models.DateField(blank=True, null=True)
    nota_giro = models.TextField(blank=True)
    caracter_giro = models.TextField(blank=True)
    fecha_desde_comision = models.DateField(blank=True, null=True)
    fecha_hasta_comision = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().GIROS
        app_label = Constants().APIREST