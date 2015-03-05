from rest_framework import serializers
from apirest.models.expedientes.legislador_firma_dictamen import LegisladorFirmaDictamen

class LegisladorFirmaDictamenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LegisladorFirmaDictamen
#         fields = ('id','fk_dictamen','fk_legislador')
