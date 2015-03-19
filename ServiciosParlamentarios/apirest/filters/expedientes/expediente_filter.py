from rest_framework.compat import django_filters
from apirest.models.expedientes.expediente import Expediente
import sys

class ExpedienteFilter(django_filters.FilterSet):
    
    # Expediente filters
    EXPEDIENTE_CHOICES = (  ('PROYECTO', 'proyecto'),
                            ('COMUNICACION', 'comunicacion'),
                            ('OBSERVACION', 'observacion'),
                            ('COMUNICACION_PEN', 'comunicacion_pen',),
                            ('SOLICITUD', 'solicitud',),)

    tipo = django_filters.MultipleChoiceFilter(choices=EXPEDIENTE_CHOICES,name="tipo")
    codigo_origen = django_filters.CharFilter(lookup_type='icontains',name="codigoorigen")
    tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipocamara")
   
    # Firmante filters
    firm_orden = django_filters.CharFilter(name="firmantes__orden")
    #firm_caracter = django_filters.CharFilter(name="firmantes__caracter")
#     firm_nota = django_filters.CharFilter(name="firmantes__nota")
    firm_cargo_pf_id = django_filters.CharFilter(name="firmantes__cargo_persona_fisica_firma_expediente_id")
    firm_apellido = django_filters.CharFilter(lookup_type='icontains',name="firmantes__fk_cargo_persona_fisica__fk_persona_fisica__historial__apellido")
    # Detalles
    tipo_proy= django_filters.CharFilter(lookup_type='icontains',name="comunicacion__tipoproy")
    tipo_proy= django_filters.CharFilter(lookup_type='icontains',name="comuniacionpen__tipoproy")
    tipo_proy= django_filters.CharFilter(lookup_type='icontains',name="observacion__tipoproy")
    tipo_proy= django_filters.CharFilter(lookup_type='icontains',name="proyecto__tipoproy")
    
    periodo = django_filters.NumberFilter(name="periodo")
    
    fecha_desde = django_filters.DateFilter(name="fecha", lookup_type='gte')
    fecha_hasta = django_filters.DateFilter(name="fecha", lookup_type='lte')

    def filter_by_date_range(self, qs, what):
        if what:
            return qs.filter(**{'total_budget__range': (int(what.start) if what.start else 0, int(what.stop) if what.stop else sys.maxint)})
        return qs

    class Meta:
        model = Expediente
        fields = ['tipo','tipo_proy','codigo_origen','tipo_camara','periodo', 'fecha_desde', 'fecha_hasta',# expedinte  
                  'firm_orden','firm_cargo_pf_id','firm_apellido', #fimante filters
                  ]
        order_by = True