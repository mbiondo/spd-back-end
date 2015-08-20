from rest_framework import viewsets
from apirest.models.organismos.bloques.bloque_estructura import BloqueEstructura
from apirest.serializers.organismos.bloques.bloque_estructura import BloqueEstructuraSerializer
from apirest.filters.organismos.bloques.bloque_estructura_filter import BloquEstructuraFilter
from django.db.models import Q
from apirest.authorizers.authorizator import has_permission
    
class BloqueEstructuraViewSet(viewsets.ReadOnlyModelViewSet):
  
    model = BloqueEstructura
    queryset = BloqueEstructura.objects.all()
    serializer_class = BloqueEstructuraSerializer
    ordering_fields = '__all__'
    filter_class = BloquEstructuraFilter
    search_fields = ('nombre','nro_integrantes','fecha_inicio','fecha_fin','tipo_camara','nota','sigla')    
                 
    @has_permission                 
    def list(self, request, *args, **kwargs):
        """
        Lista las estructuras de los bloques.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve una estructura de bloque por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
