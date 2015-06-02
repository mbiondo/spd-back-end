from rest_framework.compat import django_filters
from apirest.models.citacion import Citacion
from apirest.filters.custom_filter_list import CustomFilterList

class CitacionFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")
    lugar = django_filters.CharFilter(lookup_type='icontains',name="fk_lugar__nombre")
    estado = django_filters.CharFilter(lookup_type='icontains',name="estado__valor")
    
    visibilidad = django_filters.NumberFilter(name="visibilidad")
    
    fecha_desde = django_filters.DateTimeFilter(lookup_type='gte',name="fecha")
    fecha_hasta = django_filters.DateTimeFilter(lookup_type='lte',name="fecha")
    
    comision = django_filters.CharFilter(lookup_type='icontains',name="comisiones__comision_hist__nombre")
        
    class Meta:
        model = Citacion
        fields = ['id','lugar', 'estado', 'visibilidad','fecha_desde','fecha_hasta','comision']