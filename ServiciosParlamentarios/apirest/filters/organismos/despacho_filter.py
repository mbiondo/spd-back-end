from rest_framework.compat import django_filters
from apirest.models.organismos.despacho import Despacho
from apirest.filters.custom_filter_list import CustomFilterList

class DespachoFilter(django_filters.FilterSet):
    
    # Despacho filters.
    id = CustomFilterList(name="id", lookup_type="in")
    tipo = django_filters.CharFilter(lookup_type='icontains',name="tipo")
    numero = django_filters.NumberFilter(name="numero")
    anio = django_filters.NumberFilter(name="anio")
    tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipo_camara")
      
    class Meta:
        model = Despacho
        fields = ['id','tipo','numero','anio','tipo_camara',]
        
        