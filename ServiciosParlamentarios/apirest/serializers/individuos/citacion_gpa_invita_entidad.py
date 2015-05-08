from rest_framework import serializers
from apirest.models.relaciones.citacion_gpa_invita_entidad import CitacionGpaInvitaEntidad

class CitacionGpaInvitaEntidadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CitacionGpaInvitaEntidad

