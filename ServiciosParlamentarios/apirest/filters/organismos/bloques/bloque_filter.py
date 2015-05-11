from rest_framework.compat import django_filters
from apirest.models.organismos.bloques.bloque import Bloque
from django.db.models import Q

class BloqueFilter(django_filters.FilterSet):
      
    nombre = django_filters.CharFilter(lookup_type='icontains',name="nombre")
    tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipo_camara")
    
    class Meta:
        model = Bloque
        fields = ['nombre','tipo_camara']
        
# def fecha_filter( queryset, value):
# 
#     filtered_qs = queryset
#     
#     if value:                                    
#         filtered_qs = queryset.filter( Q(finicio__lte=value), Q(ffin__isnull=True) | Q(ffin__gt=value))
#                                  
#     return filtered_qs        
#         
# class BloqueDetalleFilter(django_filters.FilterSet):
#     
#     nombre = django_filters.CharFilter(lookup_type='icontains', name='nombre')
#     nombre_legislador = django_filters.CharFilter(lookup_type='icontains', name='integrantes__nombre_legislador')
#     tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipocamara")
#     fecha = django_filters.CharFilter(action=fecha_filter)
#     
#     class Meta:
#         model = Bloque
#         fields = ['nombre', 'nombre_legislador', 'tipo_camara', 'fecha']
        