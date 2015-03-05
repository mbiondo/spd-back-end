from rest_framework import serializers
from apirest.models.expedientes.comunicacion_entidad import ComunicacionEntidad

class ComunicacionEntidadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComunicacionEntidad 
#         fields = ('id','fk_entidad','fk_comunicacion')
            