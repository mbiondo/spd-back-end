from rest_framework import viewsets, filters
from apirest.models.publicaciones.orden_dia import OrdenDia
from apirest.serializers.publicaciones.orden_dia import OrdenDiaSerializer
from apirest.filters.publicaciones.orden_dia import OrdenDiaFilter
from apirest.authorizers.authorizator import has_permission

class OrdenDiaViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = OrdenDia
    serializer_class = OrdenDiaSerializer
    filter_class = OrdenDiaFilter
    ordering_fields = '__all__'
    search_fields = ()
    
    def get_queryset(self):
        message = self.request.GET.get('publicadas')
        queryset = None
        if message == 'True':
            queryset = OrdenDia.objects.filter(fecha_art113__isnull=False)
        else:
            queryset = OrdenDia.objects.all()
        
        return queryset
        
    @has_permission    
    def list(self, request, *args, **kwargs):
        """
        Lista todos las ordenes del dia
        """      
        
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)

    @has_permission    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve una orden del dia. 
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)