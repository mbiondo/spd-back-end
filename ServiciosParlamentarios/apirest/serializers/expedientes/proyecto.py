from rest_framework import serializers
from apirest.models.expedientes.proyecto import Proyecto

class ProyectoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Proyecto 
#         fields = ('id','estado','tipoproy','subtipoproy','codigodigesto')
        
        
class ProyectoChildSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Proyecto 
#         fields = ('id','estado','tipoproy','subtipoproy','codigodigesto')  