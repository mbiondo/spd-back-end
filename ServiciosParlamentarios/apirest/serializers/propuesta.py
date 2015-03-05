from rest_framework import serializers
from apirest.models.propuesta import Propuesta

class PropuestaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Propuesta
#         fields = ('id','fk_dictamen','nroorden','tipo','sumario')