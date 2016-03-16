from rest_framework import serializers
from apirest.models.citacion import Citacion
from apirest.serializers.relaciones.citacion_comision import CitacionComisionSerializer 
from apirest.serializers.citacion_temario import CitacionTemarioSerializer

class CitacionSerializer(serializers.ModelSerializer):

	citacion_comision = CitacionComisionSerializer(many=True)
	estado = serializers.StringRelatedField()
	temario = CitacionTemarioSerializer(many=True)
	
	class Meta():
		model = Citacion
		fields = ('id','fk_comision_cabecera','fk_lugar','estado','fecha','resumen','observaciones',
				  'visibilidad','reunion_conjunta','citacion_comision','invitados','temario')
		
class CitacionComsionReunion(serializers.ModelSerializer):
	
	class Meta():
		model = Citacion
		fields = ('id','proyectos')