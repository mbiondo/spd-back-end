from rest_framework import serializers
from apirest.models.aux_estado import AuxEstado

class AuxEstadoSerializer(serializers.ModelSerializer):

    class Meta():
        model = AuxEstado
        fields = ('id','valor','entidad','orden','descripcion','fdesde','fhasta')
        
