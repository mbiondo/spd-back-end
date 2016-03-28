from rest_framework import serializers
from apirest.models.expedientes.expediente import Expediente
from apirest.serializers.db_views.firmantes import FirmanteSerializer
from apirest.serializers.db_views.giros import GirosSerializer

class ExpedienteSerializer(serializers.ModelSerializer):
    giros = GirosSerializer(many=True)
    firmantes = FirmanteSerializer(many=True)

    class Meta:
        model = Expediente
        fields = ('id','codigo_exp','codigo_num','codigo_origen','codigo_anio','sumario','tipo_camara','tipo','codigo_estado',
                  'fecha_caducidad','fecha','periodo','titulo','voces', 'giros', 'firmantes')