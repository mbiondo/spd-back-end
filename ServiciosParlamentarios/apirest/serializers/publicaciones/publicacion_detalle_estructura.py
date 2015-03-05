from rest_framework import serializers
from apirest.models.publicaciones.publicacion_detalle_estructura import PublicacionDetalleEstructura

class PublicacionDetalleEstructuraSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PublicacionDetalleEstructura
#         fields = ('id','fk_publicacion_estructura','ordenitem','item','tituloitem','ordensubitem',
#                   'subitem','titulosubitem','contadorsubitem')