from rest_framework.compat import django_filters
from apirest.filters.custom_filter_list import CustomFilterList
from apirest.models.mocion import Mocion

class MocionFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")      
    tipo = django_filters.CharFilter(lookup_type='icontains',name="tipo")
    descripcion = django_filters.CharFilter(lookup_type='icontains',name="descripcion")
    resultado = django_filters.CharFilter(lookup_type='icontains',name="resultado")
    dictamen = django_filters.CharFilter(lookup_type='icontains',name="dictamen")
        
    class Meta:
        model = Mocion
        fields = ['id','tipo','descripcion','resultado','dictamen']
