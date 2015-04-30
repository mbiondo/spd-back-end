from rest_framework import serializers
from apirest.models.expedientes.expediente import Expediente
from apirest.serializers.db_views.firmantes import FirmanteSerializer
# from apirest.serializers.db_views.giros import GirosSerializer
from apirest.serializers.giro import GiroSerializer

class ExpedienteSerializer(serializers.ModelSerializer):
    
#     firmantes = FirmanteSerializer(many=True)    
#     giros = GiroSerializer(many=True)
    
    class Meta:
        model = Expediente
        fields = ('id','codigoexp','codigonum','codigoorigen','codigoanio','sumario','tipocamara','tipo','codigoestado',
                  'fechacaducidad','fecha','periodo','titulo','voces','firmantes','giros')
