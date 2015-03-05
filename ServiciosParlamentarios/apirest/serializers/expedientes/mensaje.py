from rest_framework import serializers
from apirest.models.expedientes.mensaje import Mensaje

class MensajeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mensaje
#         fields = ('id','fk_expediente','num','anio','fecha')
