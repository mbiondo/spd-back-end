from rest_framework import serializers
from apirest.serializers.organismos.comisiones.comision import ComisionSerializer
from apirest.models.citacion import Citacion
from apirest.serializers.db_views.comisiones_actuales import ComisionesActualesSerializer

class CitacionSerializer(serializers.ModelSerializer):

    fk_comision_cabecera = ComisionSerializer()
#     comisiones = ComisionSerializer(many=True)
    comisiones = ComisionesActualesSerializer(many=True)
    
    class Meta():
        model = Citacion
        fields = ('id','fk_comision_cabecera','fk_lugar','fk_estado','fecha','resumen','observaciones',
                  'visibilidad','breunionconjunta', 'comisiones')