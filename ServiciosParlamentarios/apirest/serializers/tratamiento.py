from rest_framework import serializers
from apirest.models.tratamiento import Tratamiento

class TratamientoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tratamiento
#         fields = ('id','tipo','orden','resumen','bfueradetemario','bsobretablas')