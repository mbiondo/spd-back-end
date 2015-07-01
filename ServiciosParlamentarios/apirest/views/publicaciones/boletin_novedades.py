from rest_framework import viewsets, filters
from apirest.models.publicaciones.boletin_novedades import BoletinNovedades
from apirest.serializers.publicaciones.boletin_novedades import BoletinNovedadesSerializer
from apirest.filters.publicaciones.boletin_novedades import BoletinNovedadesFilter
from apirest.authorizers.authorizator import has_permission

class BoletinNovedadesViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = BoletinNovedades
    queryset = BoletinNovedades.objects.all()
    serializer_class = BoletinNovedadesSerializer
    filter_class = BoletinNovedadesFilter
    ordering_fields = '__all__'
#     search_fields = ()
        
    @has_permission    
    def list(self, request, *args, **kwargs):
        """
        Lista todos los boletines de novedades tratados. (BN)
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)

    @has_permission    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve un boletin de novedades (BN) solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)