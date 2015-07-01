from rest_framework import viewsets
from apirest.models.aux_estado import AuxEstado
from apirest.serializers.aux_estado import AuxEstadoSerializer
from apirest.filters.aux_estado_filter import AuxEstadoFilter
from apirest.authorizers.authorizator import has_permission

class AuxEstadoViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset =  AuxEstado.objects.all()
    serializer_class = AuxEstadoSerializer
    filter_class = AuxEstadoFilter    
    ordering_fields = 'orden'

    @has_permission        
    def list (self, request, *args, **kwargs):
        """
        Lista todos los estados.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)

    @has_permission
    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve un estado determinado por su id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    