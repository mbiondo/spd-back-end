from rest_framework import viewsets, filters
from apirest.models.publicaciones.boletin_asuntos_tratados import BoletinAsuntosTratados
from apirest.serializers.publicaciones.boletin_asuntos_tratados import BoletinAsuntosTratadosSerializer
from apirest.filters.publicaciones.boletin_asuntos_tratados import BoletinAsuntosTratadosFilter

class BoletinAsuntosTratadosViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = BoletinAsuntosTratados
    queryset = BoletinAsuntosTratados.objects.all()
    serializer_class = BoletinAsuntosTratadosSerializer
    filter_class = BoletinAsuntosTratadosFilter
    ordering_fields = '__all__'
    search_fields = ()
        
    
    def list(self, request, *args, **kwargs):
        """
        Lista todos los boletines de asuntos tratados. (BAT)
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve un boletin de asuntos tratados (BAT) solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)