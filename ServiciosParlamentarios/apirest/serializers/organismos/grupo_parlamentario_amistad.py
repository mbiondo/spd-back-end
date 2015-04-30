from rest_framework import serializers
from apirest.models.organismos.grupo_parlamentario_amistad import GrupoParlamentarioAmistad

class GrupoParlamentarioAmistadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GrupoParlamentarioAmistad
