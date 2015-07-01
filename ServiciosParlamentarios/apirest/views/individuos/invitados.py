from rest_framework import viewsets
from apirest.models.relaciones.citacion_invita_entidad import CitacionInvitaEntidad
from apirest.serializers.individuos.citacion_invita_entidad import CitacionInvitaEntidadSerializer
from apirest.filters.individuos.invitado_filter import InvitadoFilter
from apirest.authorizers.authorizator import has_permission

class CitacionInvitaEntidadViewSet(viewsets.ReadOnlyModelViewSet):
  
    queryset = CitacionInvitaEntidad.objects.all()
    serializer_class = CitacionInvitaEntidadSerializer
    filter_class = InvitadoFilter
    
    @has_permission    
    def list(self, request, *args, **kwargs):
        """
        Lista todos los invitados.        
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve el invitado solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    