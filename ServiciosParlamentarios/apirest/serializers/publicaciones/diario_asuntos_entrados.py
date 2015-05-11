from rest_framework import serializers
from apirest.models.publicaciones.diario_asuntos_entrados import DiarioAsuntosEntrados

class DiarioAsuntosEntradosSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = DiarioAsuntosEntrados