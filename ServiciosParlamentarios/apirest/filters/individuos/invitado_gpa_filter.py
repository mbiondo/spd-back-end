from rest_framework.compat import django_filters
from apirest.filters.custom_filter_list import CustomFilterList
from apirest.models.relaciones.citacion_gpa_invita_entidad import CitacionGpaInvitaEntidad

class InvitadoGpaFilter(django_filters.FilterSet):

    id = CustomFilterList(name="id", lookup_type="in")
    nombre = django_filters.CharFilter(lookup_type='icontains',name="nombre")
      
    class Meta:
        model = CitacionGpaInvitaEntidad
        fields = ['id', 'nombre']
        


