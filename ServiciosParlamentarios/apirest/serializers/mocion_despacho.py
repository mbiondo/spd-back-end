from rest_framework import serializers
from apirest.models.relaciones.mocion_despacho import MocionSobreDespacho

class MocionSobreDespachoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MocionSobreDespacho
#         fields = ('id','fk_despacho','fk_mocion')