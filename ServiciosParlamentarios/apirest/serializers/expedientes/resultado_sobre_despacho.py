from rest_framework import serializers
from apirest.models.expedientes.resultado_sobre_despacho import ResultadoSobreDespacho

class ResultadoSobreDespachoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ResultadoSobreDespacho
#         fields = ('id','fk_despacho','fk_resultado')