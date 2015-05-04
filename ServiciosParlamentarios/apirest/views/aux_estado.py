from rest_framework import viewsets
from apirest.models.aux_estado import AuxEstado
from apirest.serializers.aux_estado import AuxEstadoSerializer

class AuxEstadoViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset =  AuxEstado.objects.all()
    serializer_class = AuxEstadoSerializer
    
    def list (self, request, *args, **kwargs):
        """
        Lista todos los estados.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)

    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve un estado determinado por su id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    