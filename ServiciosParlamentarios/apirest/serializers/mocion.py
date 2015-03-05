from rest_framework import serializers
from apirest.models.mocion import Mocion

class MocionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mocion
#         fields = ('id','fk_camara_reunion','tipo','descripcion','fechahora','resultado','orden','nivel','dictamen')