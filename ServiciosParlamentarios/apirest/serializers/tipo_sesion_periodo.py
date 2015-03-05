from rest_framework import serializers
from apirest.models.tipo_sesion_periodo import TipoSesionPeriodo

class TipoSesionPeriodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoSesionPeriodo
#         fields = ('id','fk_periodo','finicio','ffin','tipo')