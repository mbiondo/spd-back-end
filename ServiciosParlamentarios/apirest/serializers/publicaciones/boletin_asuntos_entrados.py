from rest_framework import serializers
from apirest.models.publicaciones.boletin_asuntos_entrados import BoletinAsuntosEntrados

class BoletinAsuntosEntradosSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = BoletinAsuntosEntrados
    