from rest_framework import serializers
from apirest.models.individuos.funcionario import Funcionario

class FuncionarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Funcionario
#         fields = ('id','finicio','ffin','cargo')