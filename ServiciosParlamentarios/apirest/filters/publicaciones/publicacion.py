from rest_framework.compat import django_filters
from apirest.models.publicaciones.publicacion import Publicacion
from apirest.filters.custom_filter import CustomFilterList

class PublicacionFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")
    fecha_impresion = django_filters.DateTimeFilter(name="fecha_impresion")
    tipo = django_filters.CharFilter(lookup_type='icontains',name="tipo")
    visibilidad = django_filters.NumberFilter(lookup_type='icontains',name="visibilidad")
            
    class Meta:
        model = Publicacion
        fields = ['id','visibilidad', 'tipo','fecha_impresion']