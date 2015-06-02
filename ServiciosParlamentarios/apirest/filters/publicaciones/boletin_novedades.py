from rest_framework.compat import django_filters
from apirest.models.publicaciones.boletin_novedades import BoletinNovedades
from apirest.filters.custom_filter_list import CustomFilterList

class BoletinNovedadesFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")
    tipo = django_filters.CharFilter(lookup_type='icontains',name="tipo")
    fecha_hora_cierre = django_filters.DateTimeFilter(name="fecha_hora_cierre")
    numero = django_filters.NumberFilter(name="numero")
    tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipo_camara")
            
    class Meta:
        model = BoletinNovedades
        fields = ['id','tipo', 'fecha_hora_cierre','numero','tipo_camara']