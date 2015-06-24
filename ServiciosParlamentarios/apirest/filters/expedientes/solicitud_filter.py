from rest_framework.compat import django_filters
from apirest.models.expedientes.solicitud import Solicitud
from apirest.filters.expedientes.expediente_filter import ExpedienteFilter

class SolicitudFilter(ExpedienteFilter):

    subtipo = django_filters.CharFilter(lookup_type='icontains',name="subtipo")

    class Meta:
        model = Solicitud
        fields = ['subtipo']