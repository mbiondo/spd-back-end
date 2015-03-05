from rest_framework import serializers
from apirest.models.expedientes.expediente_origina_despacho import ExpedienteOriginaDespacho

class ExpedienteOriginaDespachoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExpedienteOriginaDespacho
#         fields = ('id','fk_expediente','fk_despacho','orden','bsolovista')