from __future__ import unicode_literals
from django.db import models
from apirest.models.cargos.cargo_persona_fisica import CargoPersonaFisica
from apirest.utils.constants import Constants

class Funcionario(models.Model):
    id = models.ForeignKey(CargoPersonaFisica, primary_key=True, db_column='funcionario_id',unique=True)
    fecha_inicio = models.DateField(db_column='finicio')
    fecha_fin = models.DateField(blank=True, null=True,db_column='ffin')
    cargo = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().FUNCIONARIO
        app_label = Constants().APIREST