from rest_framework.compat import django_filters
from django.db.models import Q
from apirest.models.organismos.comisiones.comision import Comision
       
def fecha_filter( queryset, value):

    filtered_qs = queryset
    
    if value:                                    
        filtered_qs = queryset.filter( Q(fecha_inicio__lte=value), Q(fecha_fin__isnull=True) | Q(fecha_fin__gt=value))
                                 
    return filtered_qs

class ComisionFilter(django_filters.FilterSet):
    
    caracter = django_filters.CharFilter(name='caracter')
    tipo_camara = django_filters.CharFilter(name='tipo_camara')
    fecha = django_filters.CharFilter(action=fecha_filter)
    
    fecha_desde = django_filters.DateTimeFilter(lookup_type='gte',name="comision_hist__fecha_desde")
    fecha_hasta = django_filters.DateTimeFilter(lookup_type='lte',name="comision_hist__fecha_hasta")
    
    nombre = django_filters.CharFilter(lookup_type='icontains', name='comision_hist__nombre')
    
    class Meta:
        model = Comision
        fields = [ 'caracter', 'tipo_camara','fecha','fecha_desde', 'fecha_hasta', 'nombre']