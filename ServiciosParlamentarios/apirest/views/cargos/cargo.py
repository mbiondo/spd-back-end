from rest_framework import viewsets, filters
from apirest.models.cargos.cargo import Cargo
from apirest.serializers.cargos.cargo import CargoSerializer
from apirest.filters.cargo_filter import CargoFilter
from apirest.authorizers.authorizator import HasPermission,\
    hand_unauthorized_exc

# class CargoViewSet(viewsets.ReadOnlyModelViewSet):
class CargoViewSet(viewsets.ModelViewSet):    
    
    model = Cargo
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    filter_class = CargoFilter
    ordering_fields = ('descripcion',)
    search_fields = ('descripcion',)
    permission_classes = (HasPermission,)
    
    #get all
    def list(self, request, *args, **kwargs):
        """
        Lista todos los cargos ordenados por id.
        \n
        Filtros posible:\n
        -descripcion=[cargo]
        """
        return viewsets.ModelViewSet.list(self, request, *args, **kwargs)
    
    #get by id
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve el cargo solicitado por id.
        """
        return viewsets.ModelViewSet.retrieve(self, request, *args, **kwargs)

    #post
    def create(self, request, *args, **kwargs):
        """
        Crea un nuevo cargo.
        """
        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)
    
    #put    
    def update(self, request, pk=None, *args, **kwargs):
        """
        Actualiza un cargo completo.
        """
        return viewsets.ModelViewSet.update(self, request, *args, **kwargs)

    #patch
    def partial_update(self, request, pk=None, *args, **kwargs):
        """
        Actualiza campos de un cargo.
        """
        return viewsets.ModelViewSet.partial_update(self, request, *args, **kwargs)

    #delete
    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Elimina un cargo.
        """
        return viewsets.ModelViewSet.destroy(self, request, *args, **kwargs)

    @hand_unauthorized_exc
    def handle_exception(self, exc):
        print 'HOLA'
        super(CargoViewSet, self).handle_exception(exc)        
        