from rest_framework import serializers
from apirest.models.expedientes.comunicacion_pen import ComunicacionPen

class ComunicacionPenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComunicacionPen 
        fields = ('id','codigo_exp','codigo_num','codigo_origen','codigo_anio','sumario','tipo_camara','tipo',
                  'codigo_estado','fecha_caducidad','fecha','periodo','titulo','voces','subtipo') 

class ComunicacionChildPenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComunicacionPen 
