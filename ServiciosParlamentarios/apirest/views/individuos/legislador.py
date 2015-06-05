from rest_framework import viewsets
from apirest.models.individuos.legislador import Legislador
from apirest.serializers.individuos.legislador import LegisladorSerializer
from apirest.filters.individuos.legislador_filter import LegisladorFilter

class LegisladorViewSet(viewsets.ReadOnlyModelViewSet):
  
    queryset = Legislador.objects.all()
    serializer_class = LegisladorSerializer
    filter_class = LegisladorFilter
    
    def list(self, request, *args, **kwargs):
        """
        Lista todos los legisladores ordenados por id.        
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve el legislador solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)

