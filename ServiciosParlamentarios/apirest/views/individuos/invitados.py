from rest_framework import viewsets
from apirest.models.relaciones.citacion_invita_entidad import CitacionInvitaEntidad
from apirest.serializers.individuos.citacion_invita_entidad import CitacionInvitaEntidadSerializer

class CitacionInvitaEntidadViewSet(viewsets.ReadOnlyModelViewSet):
  
    queryset = CitacionInvitaEntidad.objects.all()
    serializer_class = CitacionInvitaEntidadSerializer

    
    def list(self, request, *args, **kwargs):
        """
        Lista todos los invitados.        
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve el invitado solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    