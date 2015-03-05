from rest_framework import serializers
from apirest.models.expedientes.insistencia import Insistencia

class InsistenciaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Insistencia
#         fields = ('id','tipo','articulos')