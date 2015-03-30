from rest_framework import viewsets
from apirest.models.citacion import Citacion
from apirest.serializers.citacion import CitacionSerializer

class CitacionViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset =  Citacion.objects.all()
    serializer_class = CitacionSerializer
    
    def list (self, request, *args, **kwargs):
        """
        Lista de todas las citaciones.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)

    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve una citacion determinado por su id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    
        