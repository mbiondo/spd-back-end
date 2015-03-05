from rest_framework import serializers
from apirest.models.expedientes.temario import Temario

class TemarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Temario
#         fields = ('id')