from rest_framework import serializers
from apirest.models.organismos.bloques.interbloque import Interbloque

class InterbloqueSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Interbloque
#         fields = ('id','nombre','caracter','finicio','ffin')
