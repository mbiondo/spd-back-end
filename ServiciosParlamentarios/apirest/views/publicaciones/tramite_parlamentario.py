from rest_framework import viewsets, filters
from apirest.models.publicaciones.tramite_parlamentario import TramiteParlamentario
from apirest.serializers.publicaciones.tramite_parlamentario import TramiteParlamentarioSerializer
from apirest.filters.publicaciones.tramite_parlamentario import TramiteParlamentarioFilter


class TramiteParlamentarioViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = TramiteParlamentario
    queryset = TramiteParlamentario.objects.all()
    serializer_class = TramiteParlamentarioSerializer
    filter_class = TramiteParlamentarioFilter
    ordering_fields = '__all__'
    search_fields = ()
        
    
    def list(self, request, *args, **kwargs):
        """
        Lista todos los tramites parlamentarios.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve un tramite parlamentario solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)