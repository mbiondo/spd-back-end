from rest_framework.compat import django_filters
from apirest.filters.custom_filter import CustomFilterList
from apirest.models.relaciones.citacion_invita_entidad import CitacionInvitaEntidad

class InvitadoFilter(django_filters.FilterSet):

    id = CustomFilterList(name="id", lookup_type="in")
    nombre = django_filters.CharFilter(lookup_type='icontains',name="nombre")
      
    class Meta:
        model = CitacionInvitaEntidad
        fields = ['id', 'nombre']
        
