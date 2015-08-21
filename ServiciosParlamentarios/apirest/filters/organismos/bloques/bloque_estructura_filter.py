from rest_framework.compat import django_filters
from apirest.models.organismos.bloques.bloque_estructura import BloqueEstructura
from apirest.filters.custom_filter import CustomFilterList, FechaFilter 

class BloquEstructuraFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")
    
    legislador = django_filters.NumberFilter(name="fk_legislador")
    
    fecha = FechaFilter()
    fecha_desde = django_filters.DateTimeFilter(lookup_type='gte',name="fecha_desde")
    fecha_hasta = django_filters.DateTimeFilter(lookup_type='lte',name="fecha_hasta") 
    
    cargo = django_filters.CharFilter(lookup_type='icontains',name="cargo")
    cargo_muestra_como = django_filters.CharFilter(lookup_type='icontains',name="cargomuestracomo")
    jerarquia = django_filters.CharFilter(lookup_type='icontains',name="jerarquia")
    estado = django_filters.CharFilter(lookup_type='icontains',name="estado")
    
    class Meta:
        model = BloqueEstructura
        fields = ['id', 'legislador','fecha','fecha_desde','fecha_hasta','cargo','cargo_muestra_como','jerarquia','estado']
        