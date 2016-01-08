from rest_framework import serializers
from apirest.models.organismos.comisiones.comision import Comision
from apirest.serializers.organismos.comisiones.comision import ComisionSerializer
from apirest.models.relaciones.citacion_comision import CitacionComision

class CitacionComisionSerializer(serializers.ModelSerializer):
	
	#comision = ComisionSerializer()

	class Meta:
		model = CitacionComision
		fields = ('id','comision','citacion','orden')
		