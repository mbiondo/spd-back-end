from rest_framework import serializers
from apirest.models.expedientes.observacion import Observacion
from apirest.serializers.organismos.despacho import DespachoSerializer

class ObservacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Observacion
        fields = ('id','codigo_exp','codigo_num','codigo_origen','codigo_anio','sumario','tipo_camara','tipo','codigo_estado',
                  'fecha_caducidad','fecha','periodo','titulo','voces','fk_despacho')
        
class ObservacionChildSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Observacion
#         fields = ('id','fk_despacho')
            