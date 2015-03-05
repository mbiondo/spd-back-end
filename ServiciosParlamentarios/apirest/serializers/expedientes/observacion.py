from rest_framework import serializers
from apirest.models.expedientes.observacion import Observacion

class ObservacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Observacion
#         fields = ('id','fk_despacho')
        
class ObservacionChildSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Observacion
#         fields = ('id','fk_despacho')
            