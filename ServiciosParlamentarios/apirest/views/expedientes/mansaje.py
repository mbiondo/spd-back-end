from rest_framework import viewsets, filters
from apirest.authorizers.authorizator import has_permission
from apirest.models.expedientes.mensaje import Mensaje
from apirest.serializers.expedientes.mensaje import MensajeSerializer
from apirest.filters.expedientes.mensaje_filter import MensajeFilter

class MensajeViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = Mensaje
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    filter_class = MensajeFilter
    ordering_fields = '__all__'
    search_fields = ()
        
    @has_permission
    def list(self, request, *args, **kwargs):
        """
        Lista todos los mensajes.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve un mensaje solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)