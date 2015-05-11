from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class PersonaFisicaDetalle(models.Model):
    persona_fisica_id = models.IntegerField(blank=True, null=True, primary_key=True)
    persona_fisica_hist_id = models.IntegerField(blank=True, null=True)
    tipo_doc = models.CharField(max_length=2, blank=True,db_column='tipodoc')
    numero_doc = models.CharField(max_length=9, blank=True,db_column='numerodoc')
    fecha_nacimiento = models.DateField(blank=True, null=True,db_column='fechanacimiento')
    apellido = models.TextField(blank=True)
    nombre = models.TextField(blank=True)
    genero = models.CharField(max_length=1, blank=True)
    apellido_casada = models.TextField(blank=True,db_column='apellidocasada')
    email = models.TextField(blank=True)
    profesion = models.TextField(blank=True)
    titulo = models.TextField(blank=True)
    tratamiento = models.TextField(blank=True)
    localidad = models.TextField(blank=True)
    estado_civil = models.TextField(blank=True,db_column='estadocivil')
    telefono = models.TextField(blank=True)
    conyuge = models.TextField(blank=True)
    codigo_exp = models.CharField(max_length=14, blank=True,db_column='codigoexp')
    titulo_exp = models.TextField(blank=True,db_column='tituloexp')

    class Meta:
        managed = False
        db_table = Constants().PERSONA_FISICA_DETALLE
        app_label = Constants().APIREST