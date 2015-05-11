from rest_framework import serializers
from apirest.models.publicaciones.tramite_parlamentario import TramiteParlamentario

class TramiteParlamentarioSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = TramiteParlamentario
