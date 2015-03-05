from rest_framework import serializers
from apirest.models.expedientes.extraordinaria import Extraordinaria

class ExtraordinariaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Extraordinaria
#         fields = ('id')
    