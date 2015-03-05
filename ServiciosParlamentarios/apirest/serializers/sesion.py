from rest_framework import serializers
from apirest.models.sesion import Sesion

class SesionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sesion
#         fields = ('id','fk_tipo_sesion_periodo','tipocamara','tipo','numero','nota','benminoria')
        