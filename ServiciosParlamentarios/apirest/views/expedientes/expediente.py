from rest_framework import viewsets, filters
from apirest.models.expedientes.expediente import Expediente
from apirest.serializers.expedientes.expediente import ExpedienteSerializer
from apirest.filters.expedientes.expediente_filter import ExpedienteFilter
from apirest.authorizers.authorizator import has_permission

class ExpedienteViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = Expediente
    queryset = Expediente.objects.all()
    serializer_class = ExpedienteSerializer
    filter_class = ExpedienteFilter
    ordering_fields = '__all__'
    search_fields = ('id', 'codigo_exp', 'codigo_num', 'codigo_origen', 'codigo_anio', 'sumario', 'tipo_camara','tipo', 
                     'codigo_estado', 'fecha_caducidad','fecha', 'periodo', 'titulo', 'voces',)
        
    @has_permission
    def list(self, request, *args, **kwargs):
        """
        Lista todos los expedientes.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)

    @has_permission    
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
       
    
