from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.cargos.cargo_persona_fisica import CargoPersonaFisica
        
class Legislador(models.Model):
    id = models.ForeignKey(CargoPersonaFisica, primary_key=True, db_column='legislador_id',unique=True)
    cargo = models.TextField(blank=True) #SENADOR / DIPUTADO
    distrito = models.TextField(blank=True)
    fincorporacion = models.DateField(blank=True, null=True)
    fcese = models.DateField(blank=True, null=True)
    finicio = models.DateField()
    ffin = models.DateField(blank=True, null=True)
    nota = models.TextField(blank=True)
    matricula = models.IntegerField(blank=True, null=True)
    partido = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().LEGISLADOR     
        app_label = Constants().APIREST   