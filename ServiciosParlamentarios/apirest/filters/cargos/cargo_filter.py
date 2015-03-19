from rest_framework.compat import django_filters
from apirest.models.cargos.cargo import Cargo

class CargoFilter(django_filters.FilterSet):
      
    descripcion = django_filters.CharFilter(lookup_type='icontains',name="descripcion")
    
    class Meta:
        model = Cargo
        fields = ['descripcion',]