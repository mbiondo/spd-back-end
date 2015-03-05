from __future__ import unicode_literals
from django.db import models
from apirest.models.expedientes.dictamen import Dictamen
from apirest.models.individuos.legislador import Legislador
from apirest.utils.constants import Constants

class LegisladorFirmaDictamen(models.Model):
    id = models.IntegerField(primary_key=True,db_column='legislador_firma_dictamen_id')
    fk_dictamen = models.ForeignKey(Dictamen, db_column='fk_dictamen')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    class Meta:
        managed = False
        db_table = Constants().LEGISLADOR_FIRMA_DICTAMEN
        app_label = Constants().APIREST