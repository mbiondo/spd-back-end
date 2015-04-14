from rest_framework.compat import django_filters
from apirest.models.citacion import Citacion

class CitacionFilter(django_filters.FilterSet):
    
    fecha = django_filters.DateTimeFilter(lookup_type='icontains',name="fecha")
    temario = django_filters.CharFilter(lookup_type='icontains',name="temario")
    lugar = django_filters.CharFilter(lookup_type='icontains',name="lugar")
    visibilidad = django_filters.NumberFilter(lookup_type='icontains',name="visibilidad")

    
    
    
    class Meta:
        model = Citacion
        fields = ['fecha', 'temario', 'lucar', 'visibilidad']