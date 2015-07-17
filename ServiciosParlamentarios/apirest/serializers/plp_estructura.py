from rest_framework import serializers
from apirest.models.plp_estructura import PlpEstructura
from apirest.serializers.plp_detalle_estructura import PlpDetalleEstructuraIdSerializer 

class PlpEstructuraSerializer(serializers.ModelSerializer):
    
    detalle_estructura_id = PlpDetalleEstructuraIdSerializer(many=True)
    
    class Meta:
        model = PlpEstructura
        field = ('id','descripcion','fecha_desde','fecha_hasta','fk_plp_estructura','detalle_estructura_id')