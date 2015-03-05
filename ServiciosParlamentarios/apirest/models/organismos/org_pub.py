from __future__ import unicode_literals
from django.db import models
from apirest.models.entidad import Entidad
from apirest.utils.constants import Constants

class OrgPub(models.Model):
    id = models.ForeignKey(Entidad, primary_key=True, db_column='org_pub_id',unique=True)
    nombre = models.TextField(blank=True)
    sigla = models.TextField(blank=True)
    fk_org_pub = models.ForeignKey('self', db_column='fk_org_pub', blank=True, null=True)
    finicio = models.DateField(blank=True, null=True)
    ffin = models.DateField(blank=True, null=True)
    nota = models.TextField(blank=True)
    
    class Meta:
        managed = False
        db_table = Constants().ORG_PUB
        app_label = Constants().APIREST