from rest_framework import serializers
from apirest.models.citacion_temario import CitacionTemario

class CitacionTemarioSerializer(serializers.ModelSerializer):
        
    class Meta():
        model = CitacionTemario
        
