from rest_framework import serializers
from apirest.models.sesion import Sesion
from apirest.serializers.tipo_sesion_periodo import TipoSesionPeriodoSerializer

class SesionSerializer(serializers.ModelSerializer):
    
    fk_tipo_sesion_periodo = TipoSesionPeriodoSerializer()
    
    class Meta:
        model = Sesion
        fields = ('id','fk_tipo_sesion_periodo','fk_camara_cita','fk_camara_celebra','tipo_camara','tipo','numero','nota','en_minoria')
        