from rest_framework.compat import django_filters
from apirest.filters.custom_filter import CustomFilterList
from apirest.models.aux_estado import AuxEstado

class AuxEstadoFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")
    entidad = django_filters.CharFilter(lookup_type='icontains',name="entidad")
            
    class Meta:
        model = AuxEstado
        fields = ['id','entidad']