from rest_framework import serializers
from apirest.models.licencia import Licencia

class LicenciaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Licencia
#         fields = ('id','fechadesde','fechahasta','motivo','consueldo')
