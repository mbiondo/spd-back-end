from rest_framework import serializers
from apirest.models.cargos.cargo_persona_fisica import CargoPersonaFisica
from django.db.models import Q

class CargoPersonaFisicaSerializer(serializers.ModelSerializer):

    class Meta:
        model = CargoPersonaFisica 
#         fields = ('id','fk_persona_fisica','selector')
#         depth = 1
