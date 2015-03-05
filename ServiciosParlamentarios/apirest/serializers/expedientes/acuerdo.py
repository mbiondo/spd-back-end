from rest_framework import serializers
from apirest.models.expedientes.acuerdo import Acuerdo

class AcuerdoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Acuerdo 
        #fields = ('id')       
        