from rest_framework.compat import django_filters
from apirest.models.publicaciones.publicacion import Publicacion

class PublicacionFilter(django_filters.FilterSet):
    
    fecha_impresion = django_filters.DateTimeFilter(name="fecha_impresion")
    tipo = django_filters.CharFilter(lookup_type='icontains',name="tipo")
    visibilidad = django_filters.NumberFilter(lookup_type='icontains',name="visibilidad")
            
    class Meta:
        model = Publicacion
        fields = ['visibilidad', 'tipo','fecha_impresion']