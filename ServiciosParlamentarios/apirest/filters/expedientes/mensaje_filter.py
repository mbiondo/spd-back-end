from rest_framework.compat import django_filters
from apirest.filters.expedientes.expediente_filter import ExpedienteFilter
from apirest.models.expedientes.mensaje import Mensaje

class MensajeFilter(ExpedienteFilter):

    codigo_exp = django_filters.CharFilter(lookup_type='icontains',name="fk_expediente__codigo_exp")
    
    class Meta:
        model = Mensaje
        fields = ['codigo_exp',]