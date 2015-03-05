from rest_framework import serializers
from apirest.models.cargos.cargo import Cargo

class CargoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cargo
#         fields = ('id','descripcion',)

