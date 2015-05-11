from rest_framework.compat import django_filters
from apirest.models.publicaciones.tramite_parlamentario import TramiteParlamentario

class TramiteParlamentarioFilter(django_filters.FilterSet):
    
    fecha_hora_apertura = django_filters.DateTimeFilter(name="fecha_hora_apertura")
    fecha_hora_cierre = django_filters.DateTimeFilter(name="fecha_hora_cierre")
    numero = django_filters.NumberFilter(name="numero")
            
    class Meta:
        model = TramiteParlamentario
        fields = ['fecha_hora_apertura', 'fecha_hora_cierre','numero']