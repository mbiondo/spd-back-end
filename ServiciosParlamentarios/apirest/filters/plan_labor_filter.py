from rest_framework.compat import django_filters
from apirest.filters.custom_filter import CustomFilterList
from apirest.models.plan_labor import PlanLabor

class PlanLaborFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")      
    estado = django_filters.CharFilter(lookup_type='icontains',name="estado")
    visibilidad = django_filters.NumberFilter(name="visibilidad")
    plp_estructura = django_filters.NumberFilter(name="fk_plp_estructura")  
    sesion = django_filters.NumberFilter(name="fk_sesion")  
        
    class Meta:
        model = PlanLabor
        fields = ['id','estado','visibilidad','plp_estructura','sesion']
