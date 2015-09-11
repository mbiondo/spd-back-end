from rest_framework.compat import django_filters
from apirest.models.publicaciones.orden_dia import OrdenDia
from apirest.filters.custom_filter import CustomFilterList

class OrdenDiaFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")
    anio = django_filters.NumberFilter(name="anio")
    numero = django_filters.NumberFilter(name="numero")
    fecha_art113 = django_filters.DateTimeFilter(name="fecha_art113")
    fk_despacho = django_filters.NumberFilter(name="despacho")
    cod_proyecto = django_filters.CharFilter(lookup_type='icontains',name="despacho__proyectos__codigo_exp")
    id_proyecto = django_filters.CharFilter(lookup_type='icontains',name="despacho__proyectos__id")    
    
    class Meta:
        model = OrdenDia
        fields = ['id','anio','numero','fecha_art113','despacho','cod_proyecto','id_proyecto']