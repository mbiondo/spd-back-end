from rest_framework import serializers
from apirest.models.relaciones.mocion_expediente import MocionExpediente

class MocionExpedienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MocionExpediente
#         fields = ('id','fk_mocion','fk_expediente','orden')
