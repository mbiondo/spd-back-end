from rest_framework import serializers
from apirest.models.relaciones.tratamiento_produce_despacho import TratamientoProduceDespacho

class TratamientoProduceDespachoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TratamientoProduceDespacho
#         fields = ('id','fk_despacho','fk_tratamiento')