from rest_framework import serializers
from apirest.models.relaciones.citacion_invita_entidad import CitacionInvitaEntidad

class CitacionInvitaEntidadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CitacionInvitaEntidad