from rest_framework.compat import django_filters
from apirest.models.publicaciones.boletin_asuntos_entrados import BoletinAsuntosEntrados
from apirest.filters.custom_filter import CustomFilterList

class BoletinAsuntosEntradosFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")
    fecha_hora_apertura = django_filters.DateTimeFilter(name="fecha_hora_apertura")
    fecha_hora_cierre = django_filters.DateTimeFilter(name="fecha_hora_cierre")
    numero = django_filters.NumberFilter(name="numero")
            
    class Meta:
        model = BoletinAsuntosEntrados
        fields = ['id','fecha_hora_cierre', 'fecha_hora_apertura','numero']