from rest_framework.compat import django_filters
from apirest.models.individuos.persona_fisica import PersonaFisica
from django.db.models import Q
import datetime
from apirest.filters.custom_filter import CustomFilterList

# def cargo_filter( queryset, value):
#     
#     actual_date = datetime.date.today()
# 
#     if not value:
#         return queryset
#     else:
#                                                
#         filtered_qs = queryset.filter( Q(cargo__funcionario__cargo__icontains = value) |
#                                        Q(cargo__legislador__cargo__icontains = value),
#                                        Q(cargo__legislador__ffin__gte=actual_date) &
#                                        Q(cargo__legislador__fcese__gte=actual_date) |
#                                        Q(cargo__funcionario__ffin__gte=actual_date ) )
#                                  
#         return filtered_qs
     
class PersonaFisicaFilter(django_filters.FilterSet):
#     cargo = django_filters.CharFilter(action=cargo_filter)
    id = CustomFilterList(name="id", lookup_type="in")
    numero_doc = django_filters.CharFilter(lookup_type='icontains',name="numero_doc")
    
    #historico
    nombre = django_filters.CharFilter(lookup_type='icontains',name="historico__nombre")
    apellido = django_filters.CharFilter(lookup_type='icontains',name="historico__apellido")
    tratamiento =  django_filters.CharFilter(lookup_type='icontains',name="historico__tratamiento")
    localidad =  django_filters.CharFilter(lookup_type='icontains',name="historico__localidad")
    fecha_desde = django_filters.DateFilter(lookup_type='gte',name="historico__fecha_desde")
    fecha_hasta = django_filters.DateFilter(lookup_type='lte',name="historico__fecha_hasta")
  
    class Meta:
        model = PersonaFisica
        fields = ['id', 'numero_doc','nombre','apellido','tratamiento','localidad','fecha_desde','fecha_hasta']