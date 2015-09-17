from rest_framework import serializers
from apirest.models.db_views.firmantes import Firmantes

class FirmanteFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firmantes
        fields = ('id','proyecto','persona_fisica_id','codigo_exp','nombre_leg_func','tipo_camara','cargo','orden','distrito','nombre_del_bloque')
        
class FirmanteSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Firmantes
#         fields = ('id','proyecto','persona_fisica_id','codigo_exp','nombre_leg_func','tipo_camara','cargo','orden','distrito','nombre_del_bloque')
        fields = ('id','nombre_leg_func','distrito','nombre_del_bloque')