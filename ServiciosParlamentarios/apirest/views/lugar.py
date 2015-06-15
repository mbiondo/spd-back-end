from rest_framework import viewsets
from apirest.serializers.lugar import LugarSerializer
from apirest.models.lugar import Lugar
from apirest.filters.lugar_filter import LugarFilter

class LugarViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset =  Lugar.objects.all()
    serializer_class = LugarSerializer
    filter_class = LugarFilter
        
    def list (self, request, *args, **kwargs):
        """
        Lista todos los lugares.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)

    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve un lugar determinado por su id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    