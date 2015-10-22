from rest_framework import serializers
from apirest.models.expedientes.comunicacion_resultado import ComunicacionResultado

class ComunicacionResultadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComunicacionResultado 
#         fields = ('id','resultado','comunicacion')           
