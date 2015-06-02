from rest_framework.compat import django_filters
from apirest.models.expedientes.comunicacion import Comunicacion
from apirest.filters.custom_filter_list import CustomFilterList

class ComunicacionFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")
    tipo = django_filters.CharFilter(lookup_type='icontains',name="tipo")
    codigo_origen = django_filters.CharFilter(lookup_type='icontains',name="codigo_origen")
    tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipo_camara")
    codigo_exp = django_filters.CharFilter(lookup_type='icontains',name="codigo_exp")
    codigo_num = django_filters.CharFilter(lookup_type='icontains',name="codigo_num")
    codigo_anio = django_filters.CharFilter(lookup_type='icontains',name="codigo_anio")
    subtipo = django_filters.CharFilter(lookup_type='icontains',name="subtipo")
    fecha_recepcion = django_filters.DateFilter(name="fecha_recepcion")
    orden = django_filters.NumberFilter(name="orden")
    fecha_desde = django_filters.DateFilter(name="fecha", lookup_type='gte')
    fecha_hasta = django_filters.DateFilter(name="fecha", lookup_type='lte')
    
    class Meta:
        model = Comunicacion
        fields = ['id','subtipo','fecha_recepcion','orden','tipo','codigo_origen','tipo_camara','codigo_exp','codigo_num'
                  ,'codigo_anio','fecha_desde','fecha_hasta','fecha_caducidad','periodo']
        order_by = True