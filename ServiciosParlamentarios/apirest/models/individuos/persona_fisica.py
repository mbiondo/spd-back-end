from __future__ import unicode_literals
from django.db import models
from apirest.models.entidad import Entidad
from apirest.utils.constants import Constants
              
class PersonaFisica(models.Model):
    id = models.ForeignKey(Entidad, primary_key=True, db_column='persona_fisica_id',unique=True)
    tipo_doc = models.CharField(max_length=2, blank=True,db_column='tipodoc')
    numero_doc = models.CharField(max_length=9, blank=True,db_column='numerodoc')
    fecha_nacimiento = models.DateField(blank=True, null=True,db_column='fechanacimiento')
    
    class Meta:
        managed = False
        app_label = Constants().APIREST
        db_table = Constants().PERSONA_FISICA
