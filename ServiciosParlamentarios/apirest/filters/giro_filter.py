from rest_framework.compat import django_filters
from apirest.filters.custom_filter import CustomFilterList
from apirest.models.giro import Giro

class GiroFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")
        
    class Meta:
        model = Giro
        fields = ['id',]

