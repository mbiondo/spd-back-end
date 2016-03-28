from rest_framework import serializers
from apirest.models.expedientes.mensaje_origina_despacho import MensajeOriginaDespacho

class MensajeOriginaDespachoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MensajeOriginaDespacho
#         fields = ('id','fk_expediente','fk_despacho','orden','bsolovista')