from rest_framework import serializers
from apirest.models.suplemento import Suplemento

class SuplementoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Suplemento
#         fields = ('id','orden','sumario','fk_observacion','fk_orden_dia')