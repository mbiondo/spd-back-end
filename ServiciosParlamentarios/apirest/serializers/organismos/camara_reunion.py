from rest_framework import serializers
from apirest.models.organismos.camara_reunion import CamaraReunion

class CamaraReunionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CamaraReunion
#         fields = ('id','fk_sesion','finicio','ffin','nroreunion','bcontinuacion','bpublicacion')