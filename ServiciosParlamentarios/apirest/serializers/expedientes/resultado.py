from rest_framework import serializers
from apirest.models.expedientes.resultado import Resultado

class ResultadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Resultado
        fields = ('id','fk_debate','resultado','tipo','titulo','sumario','texto')
