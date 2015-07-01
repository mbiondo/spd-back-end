from rest_framework import viewsets
from apirest.models.citacion import Citacion
from apirest.serializers.citacion import CitacionSerializer
from apirest.filters.citacion_filter import CitacionFilter
from apirest.authorizers.authorizator import has_permission

class CitacionViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset =  Citacion.objects.all()
    serializer_class = CitacionSerializer
    filter_class = CitacionFilter

    @has_permission    
    def list (self, request, *args, **kwargs):
        """
        Lista de todas las citaciones.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission
    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve una citacion determinado por su id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    
        