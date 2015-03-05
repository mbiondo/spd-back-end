from rest_framework import serializers
from apirest.models.organismos.presidencia import PresidenciaCamara

class PresidenciaCamaraSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PresidenciaCamara
#         fields = ('id')