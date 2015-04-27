from rest_framework import serializers
from apirest.models.expedientes.dictamen import Dictamen
from apirest.serializers.organismos.despacho import DespachoSerializer

class DictamenSerializer(serializers.ModelSerializer):
    
    despacho = DespachoSerializer()
    
    class Meta:
        model = Dictamen
        fields = ('id','despacho','tipo','copete','accion','bconmodificacion')           
        
