from rest_framework import viewsets, filters
from apirest.models.publicaciones.diario_asuntos_entrados import DiarioAsuntosEntrados
from apirest.serializers.publicaciones.diario_asuntos_entrados import DiarioAsuntosEntradosSerializer
from apirest.filters.publicaciones.diario_asuntos_entrados import DiarioAsuntosEntradosFilter

class DiarioAsuntosEntradosViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = DiarioAsuntosEntrados
    queryset = DiarioAsuntosEntrados.objects.all()
    serializer_class = DiarioAsuntosEntradosSerializer
    filter_class = DiarioAsuntosEntradosFilter
    ordering_fields = '__all__'
    search_fields = ()
        
    
    def list(self, request, *args, **kwargs):
        """
        Lista todos los diarios de asuntos tratados. (DAT)
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve un diarios de asuntos entrados (DAT) solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)