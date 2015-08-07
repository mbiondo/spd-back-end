from rest_framework import serializers 
from apirest.models.organismos.comisiones.comision_reunion import ComisionReunion
from apirest.serializers.debate import DebateSerializer
from apirest.serializers.citacion import CitacionComsionReunion

class ComisionReunionSerializer(serializers.ModelSerializer):
    
    debate_comision_reunion = DebateSerializer(many=True)
    fk_citacion = CitacionComsionReunion(many=True)
    
    class Meta: 
        model = ComisionReunion
        fields = ('id','tratamientos','fk_citacion','fk_comision_cabecera','temario','fecha','lugar'
                  ,'art108par1','visibilidad','visibilidad_parte','nota','debate_comision_reunion')