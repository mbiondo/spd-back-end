from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.individuos.legislador import Legislador
from apirest.models.expedientes.observacion import Observacion

class LegisladorFirmaObservacion(models.Model):
    id = models.IntegerField(primary_key=True,db_column='legislador_firma_observacion_id')
    fk_legislador = models.ForeignKey(Legislador, db_column='fk_legislador')
    fk_observacion = models.ForeignKey(Observacion, db_column='fk_observacion')

    class Meta:
        managed = False
        db_table = Constants().LEGISLADOR_FIRMA_OBSERVACION
        app_label = Constants().APIREST