from rest_framework import serializers
from apirest.models.expedientes.expediente import Expediente

class ExpedienteSerializer(serializers.ModelSerializer):
    
#     firmantes = FirmanteSerializer(many=True)    
#     giros = GiroSerializer(many=True)
    
    class Meta:
        model = Expediente
        fields = ('id','codigoexp','codigonum','codigoorigen','codigoanio','sumario','tipocamara','tipo','codigoestado',
                  'fechacaducidad','fecha','periodo','titulo','voces','firmantes','giros','resultados')