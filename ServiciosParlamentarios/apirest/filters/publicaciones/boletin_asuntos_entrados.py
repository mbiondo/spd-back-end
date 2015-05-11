from rest_framework.compat import django_filters
from apirest.models.publicaciones.boletin_asuntos_entrados import BoletinAsuntosEntrados

class BoletinAsuntosEntradosFilter(django_filters.FilterSet):
    
    fhapertura = django_filters.DateTimeFilter(name="fhapertura")
    fhcierre = django_filters.DateTimeFilter(name="fhcierre")
    numero = django_filters.NumberFilter(name="numero")
            
    class Meta:
        model = BoletinAsuntosEntrados
        fields = ['fhapertura', 'fhcierre','numero']