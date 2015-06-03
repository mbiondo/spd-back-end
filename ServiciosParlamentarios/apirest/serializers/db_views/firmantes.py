from rest_framework import serializers
from apirest.models.db_views.firmantes import Firmantes


class FirmanteSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Firmantes
        fields = ('id','proyecto','cargo_persona_fisica_id','codigo_exp','nombre_leg_func','tipo_camara','cargo','orden','distrito','nombre_del_bloque')