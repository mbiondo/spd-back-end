from rest_framework import viewsets, filters
from apirest.models.expedientes.comunicacion_pen import ComunicacionPen
from apirest.serializers.expedientes.comunicacion_pen import ComunicacionPenSerializer
from apirest.filters.expedientes.comunicacion_pen_filter import ComunicacionPenFilter
from apirest.authorizers.authorizator import has_permission

class ComunicacionPenViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = ComunicacionPen
    queryset = ComunicacionPen.objects.all()
    serializer_class = ComunicacionPenSerializer
    filter_class = ComunicacionPenFilter
    ordering_fields = '__all__'
    search_fields = ()
        
    @has_permission
    def list(self, request, *args, **kwargs):
        """
        Lista todas las comunicaciones pen.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve una comunicacion pen solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)