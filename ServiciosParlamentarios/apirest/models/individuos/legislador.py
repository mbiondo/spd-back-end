from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.cargos.cargo_persona_fisica import CargoPersonaFisica
        
class Legislador(CargoPersonaFisica):
    legislador = models.OneToOneField(CargoPersonaFisica, parent_link=True )
#     id = models.ForeignKey(CargoPersonaFisica, primary_key=True, db_column='legislador_id',unique=True)
    cargo = models.TextField(blank=True) #SENADOR / DIPUTADO
    distrito = models.TextField(blank=True)
    fecha_incorporacion = models.DateField(blank=True, null=True,db_column='fincorporacion')
    fecha_cese = models.DateField(blank=True, null=True,db_column='fcese')
    fecha_inicio = models.DateField(db_column='finicio')
    fecha_fin = models.DateField(blank=True, null=True,db_column='ffin')
    nota = models.TextField(blank=True)
    matricula = models.IntegerField(blank=True, null=True)
    partido = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().LEGISLADOR     
        app_label = Constants().APIREST   