from rest_framework import viewsets
from apirest.authorizers.authorizator import has_permission
from apirest.models.organismos.comisiones.com_estructura import ComEstructura
from apirest.serializers.organismos.comisiones.com_estructura import ComEstructuraSerializer
from apirest.filters.organismos.comisiones.com_estructura_filter import ComEstructuraFilter

class ComEstructuraViewSet(viewsets.ReadOnlyModelViewSet):
  
    queryset = ComEstructura.objects.all()
    serializer_class = ComEstructuraSerializer
    filter_class = ComEstructuraFilter
    
    @has_permission         
    def list(self, request, *args, **kwargs):
        """
        Lista las estructuras de las comisiones.        
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission         
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve la estructura solicitada por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    