from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class ComunicacionResultado(models.Model):
    id = models.AutoField(primary_key=True,db_column='comunicacion_resultado_id')
    resultado = models.ForeignKey('Resultado', db_column='fk_resultado')
    comunicacion = models.ForeignKey('Comunicacion', db_column='fk_comunicacion')  
    
    class Meta:
        managed = False
        db_table = Constants().COMUNICACION_RESULTADO
        app_label = Constants().APIREST