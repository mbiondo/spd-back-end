from rest_framework import serializers
from apirest.models.citacion import Citacion
from apirest.serializers.organismos.comisiones.comision import ComisionSerializer 

class CitacionSerializer(serializers.ModelSerializer):

#     fk_comision_cabecera = ComisionSerializer()
#     comisiones = ComisionSerializer(many=True)
#     comisiones = ComisionesActualesSerializer(many=True)
    estado = serializers.StringRelatedField()
    
    class Meta():
        model = Citacion
        fields = ('id','fk_comision_cabecera','fk_lugar','estado','fecha','resumen','observaciones',
                  'visibilidad','reunion_conjunta','comisiones','invitados')
        
class CitacionComsionReunion(serializers.ModelSerializer):
    
    class Meta():
        model = Citacion
        fields = ('id','proyectos')