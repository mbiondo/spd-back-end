from __future__ import unicode_literals
from django.db import models
from apirest.models.expedientes.expediente import Expediente
from apirest.utils.constants import Constants
from apirest.models.expedientes.expediente_origina_despacho import ExpedienteOriginaDespacho
from apirest.models.expedientes.resultado_sobre_expediente import ResultadoSobreExpediente

class Proyecto(Expediente):

    proyecto = models.OneToOneField(Expediente, parent_link=True)
    fk_proyecto_reproduce = models.ForeignKey('self', db_column='fk_proyecto_reproduce', blank=True, null=True)
    estado = models.TextField(blank=True)
    tipo_proy = models.TextField(blank=True,db_column='tipoproy')
    subtipo_proy = models.TextField(blank=True,db_column='subtipoproy')
    codigo_digesto = models.CharField(max_length=6, blank=True,db_column='codigodigesto')
    resultados = models.ManyToManyField('Resultado',through=ResultadoSobreExpediente, related_name='resultados')
    despachos = models.ManyToManyField('Despacho',through=ExpedienteOriginaDespacho, related_name='proyectos')
    
    class Meta:
        managed = False
        db_table = Constants().PROYECTO
        app_label = Constants().APIREST