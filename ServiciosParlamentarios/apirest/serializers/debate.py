from rest_framework import serializers
from apirest.models.debate import Debate

class DebateSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Debate
#         fields = ('id','fk_camara_reunion','fecha','orden','nivel',
#                   'subnivel','letra_nivel','letra_subnivel','tipo','nota',
#                   'fk_debate_padre','bcontinuacion','textolegado')
        