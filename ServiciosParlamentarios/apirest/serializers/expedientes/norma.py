from rest_framework import serializers
from apirest.models.expedientes.norma import Norma

class NormaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Norma
#         fields = ('id')