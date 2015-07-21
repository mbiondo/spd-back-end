from rest_framework import viewsets
from apirest.serializers.sesion import SesionSerializer
from apirest.models.sesion import Sesion
from apirest.filters.sesion_filter import SesionFilter 
from apirest.authorizers.authorizator import has_permission

class SesionViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset =  Sesion.objects.all()
    serializer_class = SesionSerializer
    filter_class = SesionFilter
    
    @has_permission        
    def list (self, request, *args, **kwargs):
        """
        Lista todas las sesiones.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission
    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve una sesion determinado por su id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    