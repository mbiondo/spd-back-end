from rest_framework import serializers
from apirest.models.publicaciones.publicacion_estructura import PublicacionEstructura

class PublicacionEstructuraSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = PublicacionEstructura
#         fields = ('id','descripcion','fdesde','fhasta','tipo')
        