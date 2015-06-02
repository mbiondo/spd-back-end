from rest_framework.compat import django_filters
from apirest.models.expedientes.comunicacion import Comunicacion
from apirest.filters.expedientes.expediente_filter import ExpedienteFilter

class ComunicacionFilter(ExpedienteFilter):

    subtipo = django_filters.CharFilter(lookup_type='icontains',name="subtipo")
    fecha_recepcion = django_filters.DateFilter(name="fecha_recepcion")
    orden = django_filters.NumberFilter(name="orden")

    class Meta:
        model = Comunicacion
        fields = ['subtipo','fecha_recepcion','orden']
        order_by = True