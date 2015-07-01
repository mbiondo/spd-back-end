from rest_framework import viewsets
from apirest.models.giro import Giro
from apirest.serializers.giro import GiroSerializer
from apirest.filters.giro_filter import GiroFilter
from apirest.authorizers.authorizator import has_permission

class GiroViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset =  Giro.objects.all()
    serializer_class = GiroSerializer
    filter_class = GiroFilter

    @has_permission    
    def list (self, request, *args, **kwargs):
        """
        Lista de todos los giros.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)

    @has_permission
    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve un giro determinado por su id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)