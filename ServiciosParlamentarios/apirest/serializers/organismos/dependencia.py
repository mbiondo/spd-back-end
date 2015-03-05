from rest_framework import serializers
from apirest.models.organismos.dependencia import Dependencia

class DependenciaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dependencia
#         fields = ('id','nombre','fk_dependencia','finicio','ffin','nota')
