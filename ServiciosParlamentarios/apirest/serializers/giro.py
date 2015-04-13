from rest_framework import serializers
from apirest.models.giro import Giro
from apirest.serializers.organismos.comisiones.comision import ComisionExpedienteSerializer


class GiroSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Giro
#         fields = ('id','fk_expediente','fk_comision','orden','caracter','nota','nrogiro','fvigencia','fecha','fremito')
            

class GiroExpedienteSerializer(serializers.ModelSerializer):

    fk_comision = ComisionExpedienteSerializer() 
        
    class Meta:
        model = Giro
        fields = ('id','fk_comision','orden','caracter','nota','nrogiro','fvigencia','fecha','fremito')
        depth=1
