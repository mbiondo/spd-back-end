from rest_framework import serializers
from apirest.models.publicaciones.bat_bn import BatBn

class BatBnSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = BatBn
#         fields = ('id','fk_publicacion_estructura','numero','fhcierre','fhreunion','tipo_camara')
    