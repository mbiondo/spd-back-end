from rest_framework import serializers
from apirest.models.expedientes.comunicacion_leg import ComunicacionLeg

class ComunicacionLegSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComunicacionLeg 
        #fields = ('id','subtipo')           
    