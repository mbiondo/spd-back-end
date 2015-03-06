from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.cargos.cargo_persona_fisica import CargoPersonaFisica
from apirest.models.expedientes.expediente import Expediente

class CargoFirmante(models.Model):
    id = models.AutoField(primary_key=True,db_column='cargo_persona_fisica_firma_expediente_id')
    fk_cargo_persona_fisica = models.ForeignKey(CargoPersonaFisica, db_column='fk_cargo_persona_fisica',related_name='firmante')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente')
    orden = models.SmallIntegerField(blank=True, null=True)
    caracter = models.TextField(blank=True)
    nota = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().CARGO_PERSONA_FISICA_FIRMA_EXPEDIENTE
        app_label = Constants().APIREST
        ordering = ('orden',)