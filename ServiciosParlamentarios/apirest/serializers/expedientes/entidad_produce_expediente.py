from rest_framework import serializers
from apirest.models.expedientes.entidad_produce_expediente import EntidadProduceExpediente

class EntidadProduceExpedienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EntidadProduceExpediente
#         fields = ('id','fk_entidad','fk_expediente')