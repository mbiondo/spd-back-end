from rest_framework import viewsets
from apirest.models.expedientes.insistencia import Insistencia
from apirest.serializers.expedientes.insistencia import InsistenciaSerializer
# from apirest.filters.expedientes.resultado_filter import ResultadoFilter

class InsistenciaViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = Insistencia
    queryset = Insistencia.objects.all()
    serializer_class = InsistenciaSerializer
#     filter_class = ResultadoFilter
    ordering_fields = '__all__'
    search_fields = ('id', 'resultado','tipo','titulo','sumario','texto')
        
    
    def list(self, request, *args, **kwargs):
        """
        Lista todas las insistencias simples.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve las inisistencia simple por id. 
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)

    
