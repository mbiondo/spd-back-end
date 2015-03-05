from rest_framework import serializers
from apirest.models.relaciones.debate_despacho import DebateDespacho

class DebateDespachoSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = DebateDespacho
#         fields = ('id','fk_despacho','fk_debate','tipoconsideracion','comunicacion')
        