from rest_framework.compat import django_filters
from apirest.models.publicaciones.tramite_parlamentario import TramiteParlamentario
from apirest.filters.publicaciones.publicacion import Publicacion

class TramiteParlamentarioFilter(django_filters.FilterSet):
    
    
    fecha_hora_apertura = django_filters.DateTimeFilter(name="fecha_hora_apertura")
    fecha_hora_cierre = django_filters.DateTimeFilter(name="fecha_hora_cierre")
    numero = django_filters.NumberFilter(name="numero")
    visibilidad = django_filters.NumberFilter(lookup_type='icontains',name="visibilidad")
    fecha_impresion = django_filters.DateTimeFilter(name="fecha_impresion")
    tipo = django_filters.CharFilter(lookup_type='icontains',name="tipo")
            
    class Meta:
        model = TramiteParlamentario
        fields = ['fecha_hora_apertura', 'fecha_hora_cierre','numero']