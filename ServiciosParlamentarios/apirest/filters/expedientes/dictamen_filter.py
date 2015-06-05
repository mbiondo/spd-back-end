from rest_framework.compat import django_filters
from apirest.models.expedientes.dictamen import Dictamen
from apirest.filters.custom_filter_list import CustomFilterList

class DictamenFilter(django_filters.FilterSet):
    
    # Dictamen filters.
    id = CustomFilterList(name="id", lookup_type="in")
    tipo = django_filters.CharFilter(lookup_type='icontains',name="tipo")
    accion = django_filters.CharFilter(lookup_type='icontains',name="accion")
    con_modificacion = django_filters.CharFilter(lookup_type='icontains',name="con_modificacion")
    copete = django_filters.CharFilter(lookup_type='icontains',name="copete")
        
    # Despacho Filters. 
    # Obtener todos los dictamenes de un despacho
    despacho_numero = django_filters.NumberFilter(name="despacho__numero")    
    despacho_tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="despacho__tipo_camara")
    despacho_tipo = django_filters.CharFilter(lookup_type='icontains',name="despacho__tipo")
    despacho_anio = django_filters.NumberFilter(name="despacho__anio")
      
    class Meta:
        model = Dictamen
        fields = ['id','tipo','accion','con_modificacion','despacho_tipo_camara','despacho_tipo','despacho_numero']
