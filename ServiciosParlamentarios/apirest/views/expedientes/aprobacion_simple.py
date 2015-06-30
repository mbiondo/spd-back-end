from rest_framework import viewsets
from apirest.models.expedientes.aprobacion_simple import AprobacionSimple
from apirest.serializers.expedientes.aprobacion_simple import AprobacionSimpleSerializer
# from apirest.filters.expedientes.resultado_filter import ResultadoFilter

class AprobacionSimpleViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = AprobacionSimple
    queryset = AprobacionSimple.objects.all()
    serializer_class = AprobacionSimpleSerializer
#     filter_class = ResultadoFilter
    ordering_fields = '__all__'
    search_fields = ('id', 'resultado','tipo','titulo','sumario','texto')
        
    
    def list(self, request, *args, **kwargs):
        """
        Lista todos los resultados que son aprobaciones simples.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve un resultado que es una aprobacion simple. 
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)

    
