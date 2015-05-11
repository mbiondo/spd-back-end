from rest_framework.compat import django_filters
from apirest.models.publicaciones.boletin_novedades import BoletinNovedades

class BoletinNovedadesFilter(django_filters.FilterSet):
    
    tipo = django_filters.CharFilter(lookup_type='icontains',name="tipo")
    fecha_cierre = django_filters.DateTimeFilter(name="fecha_cierre")
    numero = django_filters.NumberFilter(name="numero")
    tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipo_camara")
            
    class Meta:
        model = BoletinNovedades
        fields = ['tipo', 'fecha_cierre','numero','tipo_camara']