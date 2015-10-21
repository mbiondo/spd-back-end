from rest_framework import serializers
from apirest.models.expedientes.comunicacion import Comunicacion

class ComunicacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comunicacion 
        fields= ('id','subtipo','fecha_recepcion','orden','codigo_exp','codigo_num','codigo_origen','codigo_anio','sumario','tipo_camara','tipo','codigo_estado',
                  'fecha_caducidad','fecha','periodo','titulo','voces')

class ComunicacionChildSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comunicacion       
