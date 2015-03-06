from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.individuos.persona_fisica import PersonaFisica

class CargoPersonaFisica(models.Model):
    id = models.AutoField(primary_key=True,db_column='cargo_persona_fisica_id')
    fk_persona_fisica = models.ForeignKey(PersonaFisica, db_column='fk_persona_fisica', related_name='cargo')
    selector = models.TextField(blank=True)  # Funcionario / Legislador

    class Meta:
        managed = False
        db_table = Constants().CARGO_PERSONA_FISICA
        app_label = Constants().APIREST
