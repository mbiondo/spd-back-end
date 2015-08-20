from rest_framework.compat import django_filters
from apirest.filters.custom_filter import CustomFilterList
from apirest.models.organismos.comisiones.com_estructura import ComEstructura

class ComEstructuraFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")
    comision_id = django_filters.NumberFilter(name="fk_comision")
    cargo = django_filters.CharFilter(lookup_type='icontains', name='cargo')
        
    fecha_desde = django_filters.DateTimeFilter(lookup_type='gte',name="fecha_desde")
    fecha_hasta = django_filters.DateTimeFilter(lookup_type='lte',name="fecha_hasta")
        
    class Meta:
        model = ComEstructura
        fields = [ 'id','comision_id', 'cargo','fecha_desde', 'fecha_hasta']