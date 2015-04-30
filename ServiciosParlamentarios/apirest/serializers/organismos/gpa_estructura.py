from rest_framework import serializers
from apirest.models.organismos.gpa_estructura import GpaEstructura

class GpaEstructuraSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GpaEstructura
