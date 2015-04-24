from rest_framework import serializers
from apirest.models.lugar import Lugar

class LugarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lugar
