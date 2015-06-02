from rest_framework.compat import django_filters
from apirest.models.expedientes.expediente import Expediente

class ExpedienteFilter(django_filters.FilterSet):
    
    fecha_caducidad = django_filters.DateFilter(name="fecha_caducidad")
    periodo = django_filters.NumberFilter(name="periodo")
     
    class Meta:
        model = Expediente
        fields = ['fecha_caducidad','periodo']
        order_by = True
        

# CODIGO PRUEBAS INICIALES
        
# Expediente filters
#     EXPEDIENTE_CHOICES = (  ('PROYECTO', 'proyecto'),
#                             ('COMUNICACION', 'comunicacion'),
#                             ('OBSERVACION', 'observacion'),
#                             ('COMUNICACION_PEN', 'comunicacion_pen',),
#                             ('SOLICITUD', 'solicitud',),)

#     tipo = django_filters.MultipleChoiceFilter(choices=EXPEDIENTE_CHOICES,name="tipo")
#     def filter_by_date_range(self, qs, what):
#         if what:
#             return qs.filter(**{'total_budget__range': (int(what.start) if what.start else 0, int(what.stop) if what.stop else sys.maxint)})
#         return qs


#         fields = ['tipo','tipo_proy','codigo_origen','tipo_camara','periodo', 'fecha_desde', 'fecha_hasta',# expedinte  
#                   'firm_orden','firm_cargo_pf_id','firm_apellido', #fimante filters
#                   ]   

#     firm_caracter = django_filters.CharFilter(name="firmantes__caracter")
#     firm_nota = django_filters.CharFilter(name="firmantes__nota")
#     firm_cargo_pf_id = django_filters.CharFilter(name="firmantes__cargo_persona_fisica_firma_expediente_id")
#     firm_apellido = django_filters.CharFilter(lookup_type='icontains',name="firmantes__fk_cargo_persona_fisica__fk_persona_fisica__historial__apellido")
