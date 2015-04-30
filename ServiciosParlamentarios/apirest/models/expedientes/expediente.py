from __future__ import unicode_literals
from django.db import models       
from apirest.utils.constants import Constants

class Expediente(models.Model):
    id = models.AutoField(primary_key=True,db_column='expediente_id')
    codigoexp = models.CharField(max_length=14, blank=True) #
    codigonum = models.CharField(max_length=5, blank=True) #
    codigoorigen = models.CharField(max_length=3, blank=True) #
    codigoanio = models.CharField(max_length=4, blank=True)
    sumario = models.TextField(blank=True)
    tipocamara = models.TextField(blank=True) #
    tipo = models.TextField(blank=True) #
    codigoestado = models.SmallIntegerField(blank=True, null=True)
    fechacaducidad = models.DateField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    periodo = models.SmallIntegerField(blank=True, null=True)
    titulo = models.TextField(blank=True)
    voces = models.TextField(blank=True)
    firmantes = models.ManyToManyField('Firmantes', related_name='firmantes')
    giros = models.ManyToManyField('Giros', related_name='giros')
    
    class Meta:
        managed = False
        db_table = Constants().EXPEDIENTE
        app_label = Constants().APIREST
        ordering = ('id',)