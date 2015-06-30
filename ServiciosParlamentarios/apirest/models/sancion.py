from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.expedientes.resultado import Resultado

class Sancion(Resultado):
       
    sancion = models.OneToOneField(Resultado, parent_link=True, related_name='sanciones')   
    nro_ley = models.CharField(max_length=5, blank=True,db_column='nroley')
    sancion_promulgada = models.TextField(blank=True,db_column='sancionpromulgada')
    sancion_vetada = models.TextField(blank=True,db_column='sancionvetada')
    codigo_digesto = models.TextField(blank=True,db_column='codigodigesto')
    insistida = models.CharField(max_length=1, blank=True,db_column='binsistida')
   
                                               
    class Meta:
        managed = False
        db_table = Constants().SANCION
        app_label = Constants().APIREST
        