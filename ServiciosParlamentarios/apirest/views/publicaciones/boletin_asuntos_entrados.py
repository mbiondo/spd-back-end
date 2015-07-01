from rest_framework import viewsets, filters
from apirest.models.publicaciones.boletin_asuntos_entrados import BoletinAsuntosEntrados
from apirest.serializers.publicaciones.boletin_asuntos_entrados import BoletinAsuntosEntradosSerializer
from apirest.filters.publicaciones.boletin_asuntos_entrados import BoletinAsuntosEntradosFilter
from apirest.authorizers.authorizator import has_permission

class BoletinAsuntosEntradosViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = BoletinAsuntosEntrados
    queryset = BoletinAsuntosEntrados.objects.all()
    serializer_class = BoletinAsuntosEntradosSerializer
    filter_class = BoletinAsuntosEntradosFilter
    ordering_fields = '__all__'
    search_fields = ()
        
    @has_permission    
    def list(self, request, *args, **kwargs):
        """
        Lista todos los boletines de asuntos entrados. (BAE)
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)

    @has_permission    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve un boletin de asuntos entrados (BAE) solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)