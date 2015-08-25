from django.db import models
from apirest.models.entidad import Entidad
from apirest.utils.constants import Constants

class PresidenciaCamara(models.Model):
    id = models.ForeignKey(Entidad, primary_key=True, db_column='presidencia_camara_id',unique=True)
    presidente = models.IntegerField(blank=True, null=True)
    fk_camara = models.IntegerField(blank=True, null=True)
    fdesde = models.DateField(blank=True, null=True)
    fhasta = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().PRESIDENCIA_CAMARA
        app_label = Constants().APIREST