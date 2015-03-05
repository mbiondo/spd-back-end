from rest_framework import serializers
from apirest.models.expedientes.comunicacion_pen import ComunicacionPen

class ComunicacionPenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComunicacionPen 
#         fields = ('id','subtipo')           

class ComunicacionChildPenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComunicacionPen 
#         fields = ('id', 'subtipo')        