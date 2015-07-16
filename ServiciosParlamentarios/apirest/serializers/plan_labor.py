from rest_framework import serializers
from apirest.models.plan_labor import PlanLabor
from apirest.serializers.plp_estructura import PlpEstructuraSerializer

class PlanLaborSerializer(serializers.ModelSerializer):
    
    fk_plp_estructura = PlpEstructuraSerializer()
    
    class Meta:
        model = PlanLabor
        field = ('id','fk_plp_estructura','fk_sesion','estado','visibilidad') 
        