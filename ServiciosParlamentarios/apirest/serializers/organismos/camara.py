from rest_framework import serializers
from apirest.models.organismos.camara import Camara

class CamaraSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Camara
#         fields = ('id','nombre','nota')


 
   
