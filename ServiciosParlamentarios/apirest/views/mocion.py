from rest_framework import viewsets
from apirest.authorizers.authorizator import has_permission
from apirest.models.mocion import Mocion
from apirest.serializers.mocion import MocionSerializer
from apirest.filters.mocion_filter import MocionFilter

class MocionViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset =  Mocion.objects.all()
    serializer_class = MocionSerializer
    ordering_fields = ('orden',)
    filter_class = MocionFilter
    
    @has_permission        
    def list (self, request, *args, **kwargs):
        """
        Lista todoas las mociones.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission
    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve una mocion determinada por su id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    