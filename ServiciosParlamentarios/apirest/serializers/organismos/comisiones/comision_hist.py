from rest_framework import serializers
from apirest.models.organismos.comisiones.comision_hist import ComisionHist

class ComisionHistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComisionHist
#         fields = ('id','fk_comision','nombre','nombrecorto','competencia','correo','cantintegrantes','fdesde',
#                   'fhasta','normacreacion','normacompetencia','orden')
