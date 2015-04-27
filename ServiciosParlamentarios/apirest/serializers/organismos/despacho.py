from rest_framework import serializers
from apirest.models.organismos.despacho import Despacho

class DespachoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Despacho
        fields = ('id','numero','anio','tipocamara','sumario','art108par2','tipo','fcaducidad','visibilidad',
                  'visibilidad','bunanimidad','tramiteespecial','bmodificaciones','textolegado')
