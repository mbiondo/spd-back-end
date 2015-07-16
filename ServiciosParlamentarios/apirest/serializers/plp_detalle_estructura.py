from rest_framework import serializers
from apirest.models.relaciones.plp_detalle_estructura import PlpDetalleEstructura

class PlpDetalleEstructuraIdSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlpDetalleEstructura
        field = ('id',)
        
class PlpDetalleEstructuraSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model  = PlpDetalleEstructura