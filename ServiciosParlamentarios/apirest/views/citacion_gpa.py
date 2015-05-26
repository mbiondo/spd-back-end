from rest_framework import viewsets
from apirest.models.citacion_gpa import CitacionGpa
from apirest.serializers.citacion_gpa import CitacionGpaSerializer
from apirest.filters.citacion_gpa_filter import CitacionGpaFilter

class CitacionGpaViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset =  CitacionGpa.objects.all()
    serializer_class = CitacionGpaSerializer
    filter_class = CitacionGpaFilter
    
    def list (self, request, *args, **kwargs):
        """
        Lista de todas las citaciones de Grupos Parlamentarios de Amistad.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)

    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve una citacion de Grupos Parlamentarios de Amistad determinado por su id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    
        