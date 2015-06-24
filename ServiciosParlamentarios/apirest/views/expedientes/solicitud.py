from rest_framework import viewsets, filters
from apirest.models.expedientes.solicitud import Solicitud 
from apirest.serializers.expedientes.solicitud import SolicitudSerializer
from apirest.filters.expedientes.solicitud_filter import SolicitudFilter


class SolicitudViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = Solicitud
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer
    filter_class = SolicitudFilter
    ordering_fields = '__all__'
        
    def list(self, request, *args, **kwargs):
        """
        Lista todas las solicitudes.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve una solicitud por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)