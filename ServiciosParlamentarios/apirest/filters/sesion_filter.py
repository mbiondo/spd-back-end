from rest_framework.compat import django_filters
from apirest.filters.custom_filter import CustomFilterList
from apirest.models.sesion import Sesion

class SesionFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="sesion", lookup_type="in")      
    tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipo_camara")
    tipo = django_filters.CharFilter(lookup_type='icontains',name="tipo")
    numero = django_filters.NumberFilter(name="numero")
    nota = django_filters.CharFilter(lookup_type='icontains',name="nota")
    en_minoria = django_filters.CharFilter(lookup_type='icontains',name="en_minoria")
    fecha_desde = django_filters.DateFilter(name="fk_tipo_sesion_periodo__fecha_inicio", lookup_type='gte')
    fecha_fin = django_filters.DateFilter(name="fk_tipo_sesion_periodo__fecha_fin", lookup_type='lte')
  
    class Meta:
        model = Sesion 
        fields = ['id','tipo_camara','tipo','numero','nota','en_minoria','fecha_desde','fecha_fin']