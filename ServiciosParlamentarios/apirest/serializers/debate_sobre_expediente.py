from rest_framework import serializers
from apirest.models.relaciones.debate_sobre_expediente import DebateSobreExpediente

class DebateSobreExpedienteSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = DebateSobreExpediente
#         fields = ('id','fk_expediente','fk_debate','orden')
        