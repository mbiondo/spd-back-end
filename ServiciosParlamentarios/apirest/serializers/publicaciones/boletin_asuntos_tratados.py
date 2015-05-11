from rest_framework import serializers
from apirest.models.publicaciones.boletin_asuntos_tratados import BoletinAsuntosTratados

class BoletinAsuntosTratadosSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = BoletinAsuntosTratados

    