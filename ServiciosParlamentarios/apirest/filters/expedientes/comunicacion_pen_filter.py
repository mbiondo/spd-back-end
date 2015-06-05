from rest_framework.compat import django_filters
from apirest.models.expedientes.comunicacion_pen import ComunicacionPen
from apirest.filters.expedientes.expediente_filter import ExpedienteFilter

class ComunicacionPenFilter(ExpedienteFilter):

    subtipo = django_filters.CharFilter(lookup_type='icontains',name="subtipo")

    class Meta:
        model = ComunicacionPen
        fields = ['subtipo']
        order_by = True