from rest_framework import serializers
from apirest.models.expedientes.resultado_sobre_expediente import ResultadoSobreExpediente

class ResultadoSobreExpedienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ResultadoSobreExpediente
#         fields = ('id','fk_resultado','fk_expediente')
