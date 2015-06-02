from rest_framework.compat import django_filters
from apirest.models.publicaciones.boletin_asuntos_tratados import BoletinAsuntosTratados
from apirest.filters.custom_filter_list import CustomFilterList

class BoletinAsuntosTratadosFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")
    fecha_hora_cierre = django_filters.DateTimeFilter(name="fecha_hora_cierre")
    numero = django_filters.NumberFilter(name="numero")
    tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipo_camara")
            
    class Meta:
        model = BoletinAsuntosTratados
        fields = ['id','fecha_hora_cierre','numero','tipo_camara']