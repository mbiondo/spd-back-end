from rest_framework import serializers
from apirest.models.entidad import Entidad

class EntidadSerializer(serializers.ModelSerializer):  
       
    class Meta:
        model = Entidad