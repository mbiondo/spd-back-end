from rest_framework.compat import django_filters
from apirest.models.publicaciones.boletin_asuntos_tratados import BoletinAsuntosTratados

class BoletinAsuntosTratadosFilter(django_filters.FilterSet):
    
    fcierre = django_filters.DateTimeFilter(name="fcierre")
    numero = django_filters.NumberFilter(name="numero")
    tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipo_camara")
            
    class Meta:
        model = BoletinAsuntosTratados
        fields = ['fapertura', 'fcierre','numero','tipo_camara']