from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants

class AuxTipoTratamiento(models.Model):
    id = models.IntegerField(primary_key=True, db_column='aux_tipo_tratamiento_id')
    tipo = models.TextField(blank=True)
    orden = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = Constants().AUX_TIPO_TRATAMIENTO
        app_label = Constants().APIREST

    def __unicode__(self):
        return '%s' % (self.tipo)