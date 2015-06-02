from rest_framework import viewsets
from apirest.models.organismos.grupo_parlamentario_amistad import GrupoParlamentarioAmistad
from apirest.serializers.organismos.grupo_parlamentario_amistad import GrupoParlamentarioAmistadSerializer
from apirest.filters.organismos.gpa_filter import GrupoParlamentarioAmistadFilter


class GpaViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = GrupoParlamentarioAmistad
    queryset = GrupoParlamentarioAmistad.objects.all()
    serializer_class = GrupoParlamentarioAmistadSerializer
    filter_class = GrupoParlamentarioAmistadFilter
    
    def list(self, request, *args, **kwargs):
        """
        Lista todos los Grupos Parlamentarios de Amistad.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve un Grupo Parlamentario de Amistad solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)