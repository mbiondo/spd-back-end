from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class GpaHist(models.Model):
    id = models.IntegerField(primary_key=True, db_column='gpa_hist_id')
    fk_grupo_parlamentario_amistad = models.ForeignKey('GrupoParlamentarioAmistad', db_column='fk_grupo_parlamentario_amistad', related_name='historico')
    nombre = models.TextField(blank=True)
    nombre_corto = models.TextField(blank=True,db_column='nombrecorto')
    competencia = models.TextField(blank=True)
    correo = models.TextField(blank=True)
    cant_integrantes = models.SmallIntegerField(blank=True, null=True,db_column='cantintegrantes')
    fecha_desde = models.DateField(db_column='fdesde')
    fecha_hasta = models.DateField(blank=True, null=True,db_column='fhasta')
    norma_creacion = models.TextField(blank=True,db_column='normacreacion')
    norma_competencia = models.TextField(blank=True,db_column='normacompetencia')
    orden = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().GPA_HIST
        app_label = Constants().APIREST   
        ordering = ('-fecha_hasta',)     