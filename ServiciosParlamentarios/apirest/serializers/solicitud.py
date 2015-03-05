from rest_framework import serializers
from apirest.models.solicitud import Solicitud

class SolicitudSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Solicitud
#         fields = ('id','subtipo')