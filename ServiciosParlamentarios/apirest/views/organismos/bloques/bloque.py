from rest_framework import viewsets
from apirest.models.organismos.bloques.bloque import Bloque
from apirest.serializers.organismos.bloques.bloque import BloqueSerializer
from apirest.filters.organismos.bloques.bloque_filter import BloqueFilter#, BloqueDetalleFilter
from django.db.models import Q
from apirest.authorizers.authorizator import has_permission

# class BloqueDetalleViewSet(viewsets.ReadOnlyModelViewSet):
#     
#     queryset = Bloque.objects.all()
#     serializer_class = BloqueIntegrantesSerializer
#     filter_class = BloqueDetalleFilter
#     
#     def list(self, request, *args, **kwargs):
#         """
#         Lista los bloques con todos sus integrantes o a una fecha determinada.
#         \n
#         Filtros posible:\n
#         -fecha=[AAAA-MM-DD]\n
#         -nombre=[Nombre bloque]\n
#         -nombre_legislador=[Nombre o apellido del legislador]\n
#         -tipo_camapara=[D,S] 
#         """
#         return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
#     
#     def retrieve(self, request, *args, **kwargs):
#         """
#         Devuelve un bloque por id con sus integrantes.
#         """
#         return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    
class BloqueViewSet(viewsets.ReadOnlyModelViewSet):
  
    model = Bloque
    queryset = Bloque.objects.all()
    serializer_class = BloqueSerializer
    filter_class = BloqueFilter
    ordering_fields = '__all__'
    search_fields = ('nombre','nro_integrantes','fecha_inicio','fecha_fin','tipo_camara','nota','sigla')    
                 
    @has_permission                 
    def list(self, request, *args, **kwargs):
        """
        Lista los bloques.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve un bloque por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
