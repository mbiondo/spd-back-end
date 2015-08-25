from rest_framework import serializers
from apirest.models.adjunto import Adjunto

class AdjuntoSerializer(serializers.ModelSerializer):

    class Meta():
        model = Adjunto
        
