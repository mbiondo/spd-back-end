from rest_framework import serializers
from apirest.models.organismos.gpa_hist import GpaHist

class GpaHistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GpaHist
        fields = ( 'id','nombre','nombre_corto','competencia','correo','cant_integrantes','fecha_desde','fecha_hasta',
                   'norma_creacion','norma_competencia','orden')
