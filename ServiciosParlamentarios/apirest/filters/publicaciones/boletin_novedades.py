from rest_framework.compat import django_filters
from apirest.models.publicaciones.boletin_novedades import BoletinNovedades

class BoletinNovedadesFilter(django_filters.FilterSet):
    
    tipo = django_filters.CharFilter(lookup_type='icontains',name="tipo")
    fcierre = django_filters.DateTimeFilter(name="fcierre")
    numero = django_filters.NumberFilter(name="numero")
    tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipo_camara")
            
    class Meta:
        model = BoletinNovedades
        fields = ['tipo', 'fcierre','numero','tipo_camara']