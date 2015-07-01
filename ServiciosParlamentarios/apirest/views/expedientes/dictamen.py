from rest_framework import viewsets, filters
from apirest.models.expedientes.dictamen import Dictamen
from apirest.serializers.expedientes.dictamen import DictamenSerializer
from apirest.filters.expedientes.dictamen_filter import DictamenFilter
from apirest.authorizers.authorizator import has_permission

class DictamenViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = Dictamen
    queryset = Dictamen.objects.all()
    serializer_class = DictamenSerializer
    filter_class = DictamenFilter
    ordering_fields = '__all__'
    search_fields = ()
        
    @has_permission
    def list(self, request, *args, **kwargs):
        """
        Lista todos los expedientes.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve el expediente solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)