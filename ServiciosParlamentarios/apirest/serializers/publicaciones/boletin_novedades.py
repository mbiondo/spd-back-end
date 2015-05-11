from rest_framework import serializers
from apirest.models.publicaciones.boletin_novedades import BoletinNovedades

class BoletinNovedadesSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = BoletinNovedades
    