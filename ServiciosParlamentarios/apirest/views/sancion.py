from rest_framework import viewsets
from apirest.models.sancion import Sancion
from apirest.serializers.sancion import SancionSerializer

class SancionViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset =  Sancion.objects.all()
    serializer_class = SancionSerializer
    
    def list (self, request, *args, **kwargs):
        """
        Lista todas las sanciones.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)

    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve una sancion determinada por su id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    