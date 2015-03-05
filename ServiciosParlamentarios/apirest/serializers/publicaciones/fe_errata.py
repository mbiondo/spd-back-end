from rest_framework import serializers
from apirest.models.publicaciones.fe_errata import FeErrata

class FeErrataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FeErrata
#         fields = ('id','orden','sumario','fk_corrige','fk_publicada')