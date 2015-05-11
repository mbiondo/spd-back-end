from rest_framework.compat import django_filters
from apirest.models.publicaciones.boletin_asuntos_entrados import BoletinAsuntosEntrados

class BoletinAsuntosEntradosFilter(django_filters.FilterSet):
    
    fecha_hora_apertura = django_filters.DateTimeFilter(name="fecha_hora_apertura")
    fecha_hora_cierre = django_filters.DateTimeFilter(name="fecha_hora_cierre")
    numero = django_filters.NumberFilter(name="numero")
            
    class Meta:
        model = BoletinAsuntosEntrados
        fields = ['fecha_hora_cierre', 'fecha_hora_apertura','numero']