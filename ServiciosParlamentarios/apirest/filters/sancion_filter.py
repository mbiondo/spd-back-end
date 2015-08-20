from rest_framework.compat import django_filters
from apirest.filters.custom_filter import CustomFilterList
from apirest.models.sancion import Sancion

class SancionFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="sancion", lookup_type="in")      
    nro_ley = django_filters.CharFilter(lookup_type='icontains',name="nro_ley")
    sancion_promulgada = django_filters.CharFilter(lookup_type='icontains',name="sancion_promulgada")
    sancion_vetada = django_filters.CharFilter(lookup_type='icontains',name="sancion_vetada")
    codigo_digesto = django_filters.CharFilter(lookup_type='icontains',name="codigo_digesto")
    insistida = django_filters.CharFilter(lookup_type='icontains',name="insistida")
     
        
    class Meta:
        model = Sancion
        fields = ['id','nro_ley','sancion_promulgada','sancion_vetada','codigo_digesto','insistida']