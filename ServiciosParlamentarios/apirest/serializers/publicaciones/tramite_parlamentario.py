from rest_framework import serializers
from apirest.models.publicaciones.tramite_parlamentario import TramiteParlamentario
from apirest.serializers.publicaciones.publicacion import PublicacionSerializer

class TramiteParlamentarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TramiteParlamentario
