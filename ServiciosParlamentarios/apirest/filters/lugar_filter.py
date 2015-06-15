from rest_framework.compat import django_filters
from apirest.filters.custom_filter_list import CustomFilterList
from apirest.models.lugar import Lugar

class LugarFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")      
    nombre = django_filters.CharFilter(lookup_type='icontains',name="nombre")
    piso = django_filters.CharFilter(lookup_type='icontains',name="piso")
    capacidad_max = django_filters.NumberFilter(name="capacidad_max")
        
    class Meta:
        model = Lugar
        fields = ['id','nombre','piso','capacidad_max']
