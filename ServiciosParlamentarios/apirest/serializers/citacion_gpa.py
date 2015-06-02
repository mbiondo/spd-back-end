from rest_framework import serializers
from apirest.models.citacion_gpa import CitacionGpa

class CitacionGpaSerializer(serializers.ModelSerializer):
    
    estado = serializers.StringRelatedField()
    
    class Meta():
        model = CitacionGpa
        
