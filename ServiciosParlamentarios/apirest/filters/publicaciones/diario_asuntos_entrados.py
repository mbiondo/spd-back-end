from rest_framework.compat import django_filters
from apirest.models.publicaciones.diario_asuntos_entrados import DiarioAsuntosEntrados

class DiarioAsuntosEntradosFilter(django_filters.FilterSet):
    
    fhapertura = django_filters.DateTimeFilter(name="fhapertura")
    fcierre = django_filters.DateTimeFilter(name="fcierre")
    numero = django_filters.NumberFilter(name="numero")
            
    class Meta:
        model = DiarioAsuntosEntrados
        fields = ['fhapertura', 'fcierre','numero']