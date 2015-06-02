from rest_framework.compat import django_filters
from apirest.models.publicaciones.tramite_parlamentario import TramiteParlamentario
from apirest.filters.custom_filter_list import CustomFilterList

class TramiteParlamentarioFilter(django_filters.FilterSet):

    id = CustomFilterList(name="id", lookup_type="in")        
    fecha_hora_apertura = django_filters.DateTimeFilter(name="fecha_hora_apertura")
    fecha_hora_cierre = django_filters.DateTimeFilter(name="fecha_hora_cierre")
    numero = django_filters.NumberFilter(name="numero")
    visibilidad = django_filters.NumberFilter(name="visibilidad")
    fecha_impresion = django_filters.DateTimeFilter(name="fecha_impresion")
            
    class Meta:
        model = TramiteParlamentario
        fields = ['id','fecha_hora_apertura', 'fecha_hora_cierre','numero','visibilidad','fecha_impresion']