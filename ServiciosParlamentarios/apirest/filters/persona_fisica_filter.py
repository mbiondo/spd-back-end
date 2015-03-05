from rest_framework.compat import django_filters
from apirest.models.individuos.persona_fisica import PersonaFisica
from django.db.models import Q
import datetime

def cargo_filter( queryset, value):
    
    actual_date = datetime.date.today()

    if not value:
        return queryset
    else:
                                               
        filtered_qs = queryset.filter( Q(cargo__funcionario__cargo__icontains = value) |
                                       Q(cargo__legislador__cargo__icontains = value),
                                       Q(cargo__legislador__ffin__gte=actual_date) &
                                       Q(cargo__legislador__fcese__gte=actual_date) |
                                       Q(cargo__funcionario__ffin__gte=actual_date ) )
                                 
        return filtered_qs
     
class PersonaFisicaFilter(django_filters.FilterSet):

    cargo = django_filters.CharFilter(action=cargo_filter)
    
    class Meta:
        model = PersonaFisica
        fields = ['cargo',]
