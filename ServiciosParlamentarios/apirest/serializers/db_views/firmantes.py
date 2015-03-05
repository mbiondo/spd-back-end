from rest_framework import serializers
from apirest.models.db_views.firmantes import Firmantes

class FirmanteSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Firmantes
        fields = ('expediente_id','persona_fisica_id','cargo_persona_fisica_id','codigoexp','nombre_leg_func','tipocamara','cargo','orden','distrito','nombre_del_bloque')