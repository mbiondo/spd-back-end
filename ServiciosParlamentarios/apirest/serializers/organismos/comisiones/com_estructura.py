from rest_framework import serializers
from apirest.models.organismos.comisiones.com_estructura import ComEstructura

class ComEstructuraSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComEstructura
#         fields = ('id','fk_comision', 'fk_legislador','cargo','cargomuestracomo','jerarquia','estado','fdesde','fhasta','nota')

class ComEstructuraIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComEstructura
        fields = ('id',)