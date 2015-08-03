from rest_framework import viewsets
from apirest.models.db_views.giros import Giros
from apirest.serializers.db_views.giros import GirosSerializer
from apirest.authorizers.authorizator import has_permission
from django.contrib.gis.gdal.prototypes.errcheck import arg_byref
from django.utils.six import iteritems

class GirosViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = Giros.objects.all()
    serializer_class = GirosSerializer
    
    @has_permission                    
    def list(self, request, *args, **kwargs):
        """
        Lista los giros de un expediente determinado.
        """               
        proyecto_pk = args[0].get('proyectos_pk')

        self.queryset = self.queryset.filter(proyecto_id = proyecto_pk)
        
        return viewsets.ReadOnlyModelViewSet.list(self, request, args[0])

    @has_permission
    def retrieve(self, request, pk=None, proyectos_pk=None):        
        """    
        Devuelve los datos de un giro para el expediente solicitado.
        """
        self.queryset = self.queryset.filter(id=pk, proyecto_id=proyectos_pk)
                
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, pk, proyectos_pk)
