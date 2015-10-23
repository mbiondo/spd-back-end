from rest_framework import serializers
from apirest.models.expedientes.mensaje import Mensaje
from apirest.serializers.expedientes.expediente import ExpedienteSerializer

class MensajeSerializer(serializers.ModelSerializer):
    
    fk_expediente = ExpedienteSerializer()
    
    class Meta:
        model = Mensaje
#         fields = ('id','fk_expediente','num','anio','fecha')
