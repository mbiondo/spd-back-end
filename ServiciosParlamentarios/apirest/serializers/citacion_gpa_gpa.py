from rest_framework import serializers
from apirest.models.relaciones.citacion_gpa_gpa import CitacionGpaGpa

class CitacionGpaGpaSerializer(serializers.ModelSerializer):

    class Meta():
        model = CitacionGpaGpa
        
