from rest_framework.compat import django_filters
from apirest.models.organismos.comisiones.comision import Comision
from apirest.filters.custom_filter import CustomFilterList,FechaFilter   

class ComisionFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")
    caracter = django_filters.CharFilter(name='caracter')
    tipo_camara = django_filters.CharFilter(name='tipo_camara')
    fecha = FechaFilter()
    
    fecha_desde = django_filters.DateTimeFilter(lookup_type='gte',name="comision_hist__fecha_desde")
    fecha_hasta = django_filters.DateTimeFilter(lookup_type='lte',name="comision_hist__fecha_hasta")
    
    nombre = django_filters.CharFilter(lookup_type='icontains', name='comision_hist__nombre')
    
    class Meta:
        model = Comision
        fields = [ 'id','caracter', 'tipo_camara','fecha','fecha_desde', 'fecha_hasta', 'nombre']