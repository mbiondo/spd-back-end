from rest_framework.compat import django_filters
from apirest.models.citacion import Citacion

class CitacionFilter(django_filters.FilterSet):
    
    lugar = django_filters.CharFilter(lookup_type='icontains',name="fk_lugar__nombre")
    estado = django_filters.CharFilter(lookup_type='icontains',name="fk_estado__valor")
    
    visibilidad = django_filters.NumberFilter(name="visibilidad")
    
    fecha_desde = django_filters.DateTimeFilter(lookup_type='gte',name="fecha")
    fecha_hasta = django_filters.DateTimeFilter(lookup_type='lte',name="fecha")
    
    comision = django_filters.CharFilter(lookup_type='icontains',name="comisiones__comision_hist__nombre")
        
    class Meta:
        model = Citacion
        fields = ['lugar', 'estado', 'visibilidad','fecha_desde','fecha_hasta','comision']