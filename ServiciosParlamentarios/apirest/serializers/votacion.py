from rest_framework import serializers
from apirest.models.votacion import Votacion

class VotacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Votacion
#         fields = ('id','orden','sumario','resultado')