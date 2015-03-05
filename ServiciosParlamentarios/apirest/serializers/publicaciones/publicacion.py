from rest_framework import serializers
from apirest.models.publicaciones.publicacion import Publicacion

class PublicacionSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Publicacion
#         fields = ('id','fk_periodo','fimpresion','tipo','visibilidad')
        