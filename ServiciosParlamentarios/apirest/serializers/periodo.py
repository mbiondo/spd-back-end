from rest_framework import serializers
from apirest.models.periodo import Periodo

class PeriodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Periodo
#         fields = ('id','nroperiodo','finicio','ffin','anioparlamentario')
    