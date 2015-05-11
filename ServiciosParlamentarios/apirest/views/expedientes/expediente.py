from rest_framework import viewsets, filters
from apirest.models.expedientes.expediente import Expediente
from apirest.serializers.expedientes.expediente import ExpedienteSerializer
from apirest.filters.expedientes.expediente_filter import ExpedienteFilter

class ExpedienteViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = Expediente
    queryset = Expediente.objects.all()
    serializer_class = ExpedienteSerializer
    filter_class = ExpedienteFilter
    ordering_fields = '__all__'
    search_fields = ('id', 'codigo_exp', 'codigo_num', 'codigo_origen', 'codigo_anio', 'sumario', 'tipo_camara','tipo', 
                     'codigo_estado', 'fecha_caducidad','fecha', 'periodo', 'titulo', 'voces',)
        
    
    def list(self, request, *args, **kwargs):
        """
        Lista todos los expedientes.
        \n
        Filtros posibles:\n
        -tipo=[PROYECTO,COMUNICACION,OBSERVACION,COMUNICACION_PEN]\n
        -tipo_proy=[RESOLUCION,DECRETO,LEY,COMUNICACION,DECLARACION]\n
        -periodo=[117,118...]\n
        -fecha_desde=[AAAA-MM-DD]\n
        -fecha_hasta=[AAAA-MM-DD]\n
        -firm_orden=[1,2..]\n
        -firm_cargo_pf_id=[persona_fisica_id]\n
        -firm_apellido=[apellido del firmante]
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve el expediente solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)

# 
# class ProyectoViewSet(ExpedienteViewSet):
#   
#     search_fields = ( 'codigoexp','codigoorigen','sumario','tipocamara','tipo','codigoestado',
#                       'fechacaducidad','fecha','periodo','titulo','voces',
#                       'firmantes__fk_cargo_persona_fisica__fk_persona_fisica__numerodoc',)
       
    
