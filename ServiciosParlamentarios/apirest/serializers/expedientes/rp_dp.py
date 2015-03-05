from rest_framework import serializers
from apirest.models.expedientes.rp_dp import RpDp

class RpDpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RpDp
#         fields = ('id')