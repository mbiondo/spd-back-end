from rest_framework import serializers
from apirest.models.expedientes.dictamen import Dictamen

class DictamenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dictamen
        fields = ('id','despacho','tipo','copete','accion','con_modificacion')       
