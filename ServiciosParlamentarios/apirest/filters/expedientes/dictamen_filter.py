from rest_framework.compat import django_filters
from apirest.models.expedientes.dictamen import Dictamen

class DictamenFilter(django_filters.FilterSet):
    
    # Dictamen filters.
    tipo = django_filters.CharFilter(lookup_type='icontains',name="tipo")
    accion = django_filters.CharFilter(lookup_type='icontains',name="accion")
    bconmodificacion = django_filters.CharFilter(lookup_type='icontains',name="bconmodificacion")
    copete = django_filters.CharFilter(lookup_type='icontains',name="copete")
        
    # Despacho Filters. 
    # Obtener todos los dictamenes de un despacho
    despacho_numero = django_filters.CharFilter(name="despacho__numero")    
    despacho_tipo_camara = django_filters.CharFilter(name="despacho__tipocamara")
    despacho_tipo = django_filters.CharFilter(name="despacho__tipo")
    despacho_anio = django_filters.CharFilter(name="despacho__anio")
      
    class Meta:
        model = Dictamen
        fields = ['tipo','accion','bconmodificacion','despacho_tipo_camara','despacho_tipo','despacho_numero']
        order_by = True
