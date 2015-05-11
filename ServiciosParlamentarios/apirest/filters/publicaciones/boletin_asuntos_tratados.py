from rest_framework.compat import django_filters
from apirest.models.publicaciones.boletin_asuntos_tratados import BoletinAsuntosTratados

class BoletinAsuntosTratadosFilter(django_filters.FilterSet):
    
    fhcierre = django_filters.DateTimeFilter(name="fhcierre")
    numero = django_filters.NumberFilter(name="numero")
    tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipo_camara")
            
    class Meta:
        model = BoletinAsuntosTratados
        fields = ['fhcierre','numero','tipo_camara']