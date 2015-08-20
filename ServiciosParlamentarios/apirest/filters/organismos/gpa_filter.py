from rest_framework.compat import django_filters
from apirest.filters.custom_filter import CustomFilterList
from apirest.models.organismos.grupo_parlamentario_amistad import GrupoParlamentarioAmistad

class GrupoParlamentarioAmistadFilter(django_filters.FilterSet):
    
    # Grupo Parlamentario de Amistad filters.
    id = CustomFilterList(name="id", lookup_type="in")
    caracter = django_filters.CharFilter(lookup_type='icontains',name="caracter")
    tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipo_camara")
    nombre = django_filters.CharFilter(lookup_type='icontains',name="historico__nombre")
    nombre_corto = django_filters.CharFilter(lookup_type='icontains',name="historico__nombre_corto")
      
    class Meta:
        model = GrupoParlamentarioAmistad
        fields = ['id','caracter','tipo_camara','nombre','nombre_corto']
                
