from rest_framework import serializers
from apirest.serializers.organismos.comisiones.comision import ComisionSerializer
from apirest.models.citacion import Citacion

class CitacionSerializer(serializers.ModelSerializer):

    fk_comision_cabecera = ComisionSerializer()
    comisiones = ComisionSerializer(many=True)
    
    class Meta():
        model = Citacion
        fields = ('id','fk_comision_cabecera','fecha','temario','lugar','visibilidad', 'comisiones')

        