from rest_framework import serializers
from apirest.models.cargos.cargo_firmante import CargoFirmante
from apirest.serializers.cargos.cargo_persona_fisica import CargoPersonaFisicaSerializer

class CargoFirmanteSerializer(serializers.ModelSerializer):
    
    fk_cargo_persona_fisica = CargoPersonaFisicaSerializer()
    
    class Meta:
        model = CargoFirmante 
        fields = ('id','fk_cargo_persona_fisica','fk_expediente','orden','caracter','nota')
