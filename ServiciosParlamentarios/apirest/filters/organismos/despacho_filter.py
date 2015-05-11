from rest_framework.compat import django_filters
from apirest.models.organismos.despacho import Despacho

class DespachoFilter(django_filters.FilterSet):
    
    # Dictamen filters.
    tipo = django_filters.CharFilter(lookup_type='icontains',name="tipo")
    numero = django_filters.CharFilter(lookup_type='icontains',name="numero")
    anio = django_filters.CharFilter(lookup_type='icontains',name="anio")
    tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipo_camara")
      
    class Meta:
        model = Despacho
        fields = ['tipo','numero','anio','tipo_camara',]
        order_by = True
        
        