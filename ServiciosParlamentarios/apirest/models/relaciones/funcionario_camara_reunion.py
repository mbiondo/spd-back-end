from __future__ import unicode_literals
from django.db import models
from apirest.utils.constants import Constants
from apirest.models.individuos.funcionario import Funcionario
from apirest.models.organismos.camara_reunion import CamaraReunion

class FuncionarioCamaraReunion(models.Model):
    id = models.AutoField(primary_key=True,db_column='funcionario_camara_reunion_id')
    fk_funcionario = models.ForeignKey(Funcionario, db_column='fk_funcionario')
    fk_camara_reunion = models.ForeignKey(CamaraReunion, db_column='fk_camara_reunion')

    class Meta:
        managed = False
        db_table = Constants().FUNCIONARIO_CAMARA_REUNION
        app_label = Constants().APIREST