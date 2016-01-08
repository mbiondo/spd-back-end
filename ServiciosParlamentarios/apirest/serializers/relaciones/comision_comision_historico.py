from rest_framework import serializers
from apirest.models.organismos.comisiones.comision_hist import ComisionHist
from apirest.serializers.organismos.comisiones.comision_hist import ComisionHistSerializer
from apirest.models.relaciones.comision_comision_historico import ComisionComisionHist

class ComisionComisionHistSerializer(serializers.ModelSerializer):
    
    comision_hist = ComisionHistSerializer()

    class Meta:
        model = ComisionComisionHist
        fields = ( 'id','fk_comision','comision_hist')
        