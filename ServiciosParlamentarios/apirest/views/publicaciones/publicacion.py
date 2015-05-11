from rest_framework import viewsets, filters
from apirest.models.publicaciones.publicacion import Publicacion
from apirest.serializers.publicaciones.publicacion import PublicacionSerializer
from apirest.filters.publicaciones.publicacion import PublicacionFilter

class PublicacionViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = Publicacion
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    filter_class = PublicacionFilter
    ordering_fields = '__all__'
    search_fields = ()
        
    
    def list(self, request, *args, **kwargs):
        """
        Lista todos las publicaciones.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve una publicacion solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)