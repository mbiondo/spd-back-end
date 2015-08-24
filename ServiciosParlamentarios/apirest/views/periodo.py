from rest_framework import viewsets
from apirest.authorizers.authorizator import has_permission
from apirest.models.periodo import Periodo
from apirest.serializers.periodo import PeriodoSerializer
from apirest.filters.periodo_filter import PeriodoFilter

class PeriodoViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset =  Periodo.objects.all()
    serializer_class = PeriodoSerializer
    filter_class = PeriodoFilter
    
    @has_permission        
    def list (self, request, *args, **kwargs):
        """
        Lista todos los periodos parlamentarios.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission
    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve un periodo por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)