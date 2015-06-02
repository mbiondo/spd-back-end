from rest_framework import serializers
from apirest.models.expedientes.comunicacion import Comunicacion

class ComunicacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comunicacion 
        field= ('id','subtipo','fecha_recepcion','orden')

class ComunicacionChildSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comunicacion 
#         fields = ('id','subtipo','fecharecepcion','orden')           
