from rest_framework import serializers
from apirest.models.expedientes.aprobacion_simple import AprobacionSimple

class AprobacionSimpleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AprobacionSimple 
        #fields = ('id', 'tipo', 'numero', 'anio')