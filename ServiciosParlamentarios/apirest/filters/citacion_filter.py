from rest_framework.compat import django_filters
from apirest.models.citacion import Citacion

class CitacionFilter(django_filters.FilterSet):
    
    temario = django_filters.CharFilter(lookup_type='icontains',name="temario")
    lugar = django_filters.CharFilter(lookup_type='icontains',name="lugar")
    visibilidad = django_filters.NumberFilter(lookup_type='icontains',name="visibilidad")
    
    fecha_desde = django_filters.DateTimeFilter(lookup_type='gte',name="fecha")
    fecha_hasta = django_filters.DateTimeFilter(lookup_type='lte',name="fecha")
    
    comision = django_filters.CharFilter(lookup_type='icontains',name="comisiones__nombre_comision")
    
    class Meta:
        model = Citacion
        fields = ['temario', 'lugar', 'visibilidad','fecha_desde','fecha_hasta','comision']