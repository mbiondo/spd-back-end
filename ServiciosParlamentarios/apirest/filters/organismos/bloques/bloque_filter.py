from rest_framework.compat import django_filters
from apirest.models.organismos.bloques.bloque import Bloque
from apirest.filters.custom_filter import CustomFilterList,FechaFilter

class BloqueFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")
    nombre = django_filters.CharFilter(lookup_type='icontains',name="nombre")
    tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipo_camara")
  
    fecha = FechaFilter()
    fecha_desde = django_filters.DateTimeFilter(lookup_type='gte',name="fecha_desde")
    fecha_hasta = django_filters.DateTimeFilter(lookup_type='lte',name="fecha_hasta")
    
    sigla = django_filters.CharFilter(lookup_type='icontains',name="sigla")
    
    class Meta:
        model = Bloque
        fields = ['id', 'nombre','fecha','fecha_desde','fecha_hasta','sigla']
        