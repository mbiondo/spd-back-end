from __future__ import unicode_literals
from django.db import models
from apirest.models.individuos.persona_fisica import PersonaFisica
from apirest.models.expedientes.expediente import Expediente
from apirest.utils.constants import Constants
 
class PersonaFisicaHist(models.Model):
    id = models.AutoField(primary_key=True, db_column='persona_fisica_hist_id')
    fk_persona_fisica = models.ForeignKey(PersonaFisica, db_column='fk_persona_fisica',related_name='historial')
    fk_expediente = models.ForeignKey(Expediente, db_column='fk_expediente', blank=True, null=True)
    nombre = models.TextField(blank=True)
    apellido = models.TextField(blank=True)
    genero = models.CharField(max_length=1, blank=True)
    apellidocasada = models.TextField(blank=True)
    email = models.TextField(blank=True)
    profesion = models.TextField(blank=True)
    titulo = models.TextField(blank=True)
    tratamiento = models.TextField(blank=True)
    direccion = models.TextField(blank=True)
    localidad = models.TextField(blank=True)
    estadocivil = models.TextField(blank=True)
    telefono = models.TextField(blank=True)
    conyuge = models.TextField(blank=True)
    fdesde = models.DateField()
    fhasta = models.DateField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().PERSONA_FISICA_HIST
        app_label = Constants().APIREST