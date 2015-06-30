from rest_framework import serializers
from apirest.models.sancion import Sancion

class SancionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sancion
        fields = ('id','fk_debate','resultado','tipo','titulo','sumario','texto'
                  ,'nro_ley','sancion_promulgada','sancion_vetada','codigo_digesto',
                  'insistida')