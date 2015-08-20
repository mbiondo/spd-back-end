from rest_framework.compat import django_filters
from django.db.models import Q

class CustomFilterList(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            values = [v for v in value.split(',')]
            return qs.filter(**{'%s__%s' % (self.name, self.lookup_type): values})
        return qs
    
class FechaFilter(django_filters.Filter):
    def filter(self,queryset, value): 
        filtered_qs = queryset
        if value:                                    
            filtered_qs = queryset.filter( Q(fecha_inicio__lte=value), Q(fecha_fin__isnull=True) | Q(fecha_fin__gt=value))                                
        return filtered_qs