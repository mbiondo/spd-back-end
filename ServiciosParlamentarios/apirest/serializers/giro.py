from rest_framework import serializers
from apirest.models.giro import Giro
from apirest.serializers.organismos.comisiones.comision import ComisionSerializer


class GiroSerializer(serializers.ModelSerializer):
    
    fk_comision = ComisionSerializer() 

    class Meta:
        model = Giro
        fields = ('id','fk_expediente','fk_comision','orden','caracter','nota','nro_giro','fecha_vigencia','fecha','fecha_remito')

class GiroExpedienteSerializer(serializers.ModelSerializer):

    fk_comision = ComisionSerializer() 
        
    class Meta:
        model = Giro
        fields = ('id','fk_comision','orden','caracter','nota','nrogiro','fecha_vigencia','fecha','fecha_remito')
        depth=1
