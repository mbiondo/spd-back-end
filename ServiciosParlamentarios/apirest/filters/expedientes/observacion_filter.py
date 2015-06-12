from rest_framework.compat import django_filters
from apirest.models.expedientes.observacion import Observacion
from apirest.filters.expedientes.expediente_filter import ExpedienteFilter

class ObservacionFilter(ExpedienteFilter):

    #Despacho filter 
    despacho_id = django_filters.NumberFilter(name="fk_despacho")
    despacho_tipo = django_filters.CharFilter(lookup_type='icontains',name="fk_despacho__tipo")
    despacho_anio = django_filters.NumberFilter(name="fk_despacho__anio")   
    despacho_numero = django_filters.NumberFilter(name="fk_despacho__numero")
    despacho_tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="fk_despacho__tipo_camara")
    despacho_art108par2 = django_filters.CharFilter(lookup_type='icontains',name="fk_despacho__art108par2")
    despacho_modificaciones = django_filters.CharFilter(lookup_type='icontains',name="fk_despacho__modificaciones")
    
    
    class Meta:
        model = Observacion
        fields = ['despacho_id','despacho_tipo','despacho_anio','despacho_numero','despacho_tipo_camara','despacho_art108par2'
                  ,'despacho_modificaciones']