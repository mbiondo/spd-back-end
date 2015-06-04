from rest_framework.compat import django_filters
from apirest.filters.custom_filter_list import CustomFilterList
from apirest.models.individuos.legislador import Legislador

class LegisladorFilter(django_filters.FilterSet):

    id = CustomFilterList(name="id", lookup_type="in")
    cargo =  django_filters.CharFilter(lookup_type='icontains',name="cargo")
    distrito = django_filters.CharFilter(lookup_type='icontains',name="distrito")
    fecha_incorporacion = django_filters.DateFilter(lookup_type='gte', name="fecha_incorporacion")
    fecha_cese = django_filters.DateFilter(lookup_type='lte',name="fecha_cese")
    fecha_inicio = django_filters.DateFilter(lookup_type='gte', name="fecha_inicio")
    fecha_fin = django_filters.DateFilter(lookup_type='lte',name="fecha_fin")
    partido = django_filters.CharFilter(lookup_type='icontains',name="partido")
    
    #filtros Persona Fisica
    nombre = django_filters.CharFilter(lookup_type='icontains',name="fk_persona_fisica__historico__nombre")
    apellido = django_filters.CharFilter(lookup_type='icontains',name="fk_persona_fisica__historico__apellido")
    genero = django_filters.CharFilter(lookup_type='icontains',name="fk_persona_fisica__historico__genero")
    
    class Meta:
        model = Legislador
        fields = ['id', 'cargo', 'distrito','fecha_incorporacion', 'fecha_cese','fecha_inicio','fecha_fin','partido',
                  'nombre','apellido','genero']
