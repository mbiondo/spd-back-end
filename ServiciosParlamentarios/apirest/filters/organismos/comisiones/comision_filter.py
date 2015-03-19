from rest_framework.compat import django_filters
from apirest.models.db_views.comision_detalle import ComisionesDetalle
from django.db.models import Q
       
def fecha_filter( queryset, value):

    filtered_qs = queryset
    
    if value:                                    
        filtered_qs = queryset.filter( Q(finicio__lte=value), Q(ffin__isnull=True) | Q(ffin__gt=value))
                                 
    return filtered_qs

               
class ComisionDetalleFilter(django_filters.FilterSet):
    
    nombre = django_filters.CharFilter(lookup_type='icontains', name='nombre_comision')
    nombre_legislador = django_filters.CharFilter(lookup_type='icontains', name='nombre_legislador')
    caracter = django_filters.CharFilter(name='caracter')
    tipo_camara = django_filters.CharFilter(name='tipocamara')
    fecha = django_filters.CharFilter(action=fecha_filter)
    
    class Meta:
        model = ComisionesDetalle
        fields = [ 'nombre', 'nombre_legislador', 'caracter', 'tipo_camara', 'fecha']
        