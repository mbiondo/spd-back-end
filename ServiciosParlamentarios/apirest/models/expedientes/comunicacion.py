from __future__ import unicode_literals
from django.db import models
from apirest.models.expedientes.expediente import Expediente
# from apirest.models.expedientes.comunicacion_resultado import ComunicacionResultado
from apirest.utils.constants import Constants
# from apirest.models.expedientes.resultado import Resultado

class Comunicacion(Expediente):
    
    comunicacion = models.OneToOneField(Expediente, parent_link=True)
    subtipo = models.TextField(blank=True)
    fecha_recepcion = models.DateField(blank=True, null=True, db_column='fecharecepcion')
    orden = models.SmallIntegerField(blank=True, null=True) 
#     resultadoscom = models.ManyToManyField('Resultado', through=ComunicacionResultado, related_name='resultadoscom')    
    
    class Meta:
        managed = False
        db_table = Constants().COMUNICACION
        app_label = Constants().APIREST