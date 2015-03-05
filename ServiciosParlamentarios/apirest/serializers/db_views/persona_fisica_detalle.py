from rest_framework import serializers
from apirest.models.db_views.persona_fisica_detalle import PersonaFisicaDetalle

class PersonaFisicaDetalleSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = PersonaFisicaDetalle