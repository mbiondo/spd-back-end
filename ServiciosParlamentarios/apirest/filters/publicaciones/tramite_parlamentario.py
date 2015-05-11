from rest_framework.compat import django_filters
from apirest.models.publicaciones.tramite_parlamentario import TramiteParlamentario

class TramiteParlamentarioFilter(django_filters.FilterSet):
    
    fhapertura = django_filters.DateTimeFilter(name="fhapertura")
    fcierre = django_filters.DateTimeFilter(name="fcierre")
    numero = django_filters.NumberFilter(name="numero")
            
    class Meta:
        model = TramiteParlamentario
        fields = ['fhapertura', 'fcierre','numero']