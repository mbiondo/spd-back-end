from rest_framework.compat import django_filters
from apirest.models.publicaciones.diario_asuntos_entrados import DiarioAsuntosEntrados

class DiarioAsuntosEntradosFilter(django_filters.FilterSet):
    
    fecha_hora_apertura = django_filters.DateTimeFilter(name="fecha_hora_apertura")
    fecha_hora_cierre = django_filters.DateTimeFilter(name="fecha_hora_cierre")
    numero = django_filters.NumberFilter(name="numero")
            
    class Meta:
        model = DiarioAsuntosEntrados
        fields = ['fecha_hora_apertura', 'fecha_hora_cierre','numero']