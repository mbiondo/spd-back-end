from rest_framework import viewsets
from apirest.models.organismos.despacho import Despacho
from apirest.serializers.organismos.despacho import DespachoSerializer
from apirest.filters.organismos.despacho_filter import DespachoFilter


class DespachoViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = Despacho
    queryset = Despacho.objects.all()
    serializer_class = DespachoSerializer
    filter_class = DespachoFilter
    ordering_fields = '__all__'
    search_fields = ()
        
    
    def list(self, request, *args, **kwargs):
        """
        Lista todos los despachos.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve un despacho solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)