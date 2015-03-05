from rest_framework import serializers
from apirest.models.expedientes.expediente_tenido_vista import ExpedienteTenidoVista

class ExpedienteTenidoVistaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExpedienteTenidoVista
#         fields = ('id','fk_tratamiento','fk_expediente')