from rest_framework.compat import django_filters
from django.db.models import Q
from apirest.models.organismos.comisiones.comision_reunion import ComisionReunion
from apirest.filters.custom_filter_list import CustomFilterList


class ComisionReunionFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")
    art108par1 = django_filters.CharFilter(lookup_type='icontains',name="art108par1")
    
    class Meta:
        model = ComisionReunion
        fields = [ 'id','art108par1',]