from rest_framework import serializers
from apirest.models.organismos.bloques.blq_interblq import BlqInterblq

class BlqInterblqSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlqInterblq
#         fields = ('id','fk_bloque','fk_interbloque','finicio','ffin','caracter')