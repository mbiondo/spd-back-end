from rest_framework import serializers
from apirest.models.sancion import Sancion

class SancionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sancion
#         fields = ('id','nroley','sancionpromulgada','sancionvetada','codigodigesto','binsistida')