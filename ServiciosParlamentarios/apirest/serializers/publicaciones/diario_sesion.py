from rest_framework import serializers
from apirest.models.publicaciones.diario_sesion import DiarioSesion

class DiarioSesionSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = DiarioSesion
        