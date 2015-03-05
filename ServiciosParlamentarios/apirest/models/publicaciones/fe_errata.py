from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.publicaciones.publicacion import Publicacion

class FeErrata(models.Model):
    id = models.ForeignKey(Publicacion, primary_key=True, db_column='fe_errata_id',unique=True)
    orden = models.IntegerField()
    sumario = models.TextField()
    fk_corrige = models.ForeignKey(Publicacion, db_column='fk_corrige', blank=True, null=True)
    fk_publicada = models.ForeignKey(Publicacion, db_column='fk_publicada', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = Constants().FE_ERRATA
        app_label = Constants().APIREST