from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class PersonaFisicaDetalle(models.Model):
    persona_fisica_id = models.IntegerField(blank=True, null=True, primary_key=True)
    persona_fisica_hist_id = models.IntegerField(blank=True, null=True)
    tipodoc = models.CharField(max_length=2, blank=True)
    numerodoc = models.CharField(max_length=9, blank=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    apellido = models.TextField(blank=True)
    nombre = models.TextField(blank=True)
    genero = models.CharField(max_length=1, blank=True)
    apellidocasada = models.TextField(blank=True)
    email = models.TextField(blank=True)
    profesion = models.TextField(blank=True)
    titulo = models.TextField(blank=True)
    tratamiento = models.TextField(blank=True)
    localidad = models.TextField(blank=True)
    estadocivil = models.TextField(blank=True)
    telefono = models.TextField(blank=True)
    conyuge = models.TextField(blank=True)
    codigoexp = models.CharField(max_length=14, blank=True)
    tituloexp = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = Constants().PERSONA_FISICA_DETALLE
        app_label = Constants().APIREST