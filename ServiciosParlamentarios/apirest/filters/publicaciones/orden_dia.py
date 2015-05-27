from rest_framework.compat import django_filters
from apirest.models.publicaciones.orden_dia import OrdenDia

class OrdenDiaFilter(django_filters.FilterSet):
    
    anio = django_filters.NumberFilter(name="anio")
    numero = django_filters.NumberFilter(name="numero")
    fecha_art113 = django_filters.DateTimeFilter(name="fecha_art113")
    fk_despacho = django_filters.NumberFilter(name="despacho")
            
    class Meta:
        model = OrdenDia
        fields = ['anio','numero','fecha_art113','despacho']