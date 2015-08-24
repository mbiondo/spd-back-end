from rest_framework.compat import django_filters
from apirest.filters.custom_filter import CustomFilterList
from apirest.models.periodo import Periodo

class PeriodoFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")     
    nro_periodo = django_filters.NumberFilter(name="nro_periodo") 
    anio_parlamentario =  django_filters.NumberFilter(name="anio_parlamentario")
    fecha_inicio = django_filters.DateFilter(name="fecha_inicio", lookup_type='gte')
    fecha_fin = django_filters.DateFilter(name="fecha_fin", lookup_type='lte')
    
    class Meta:
        model = Periodo
        fields = ['id','nro_periodo','anio_parlamentario','fecha_inicio','fecha_fin']
