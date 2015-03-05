from rest_framework import serializers
from apirest.models.expedientes.veto import Veto

class VetoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Veto
#         fields = ('id','fk_sancion','estotal')