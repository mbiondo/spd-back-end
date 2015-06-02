from rest_framework.compat import django_filters
from apirest.models.cargos.cargo import Cargo
from apirest.filters.custom_filter_list import CustomFilterList

class CargoFilter(django_filters.FilterSet):

    id = CustomFilterList(name="id", lookup_type="in")
    descripcion = django_filters.CharFilter(lookup_type='icontains',name="descripcion")
    
    class Meta:
        model = Cargo
        fields = ['id','descripcion',]