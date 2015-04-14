from rest_framework import viewsets, filters
from apirest.models.cargos.cargo import Cargo
from apirest.serializers.cargos.cargo import CargoSerializer
from apirest.filters.cargos.cargo_filter import CargoFilter
from apirest.authorizers.authorizator import has_permission

# class CargoViewSet(viewsets.ReadOnlyModelViewSet):
class CargoViewSet(viewsets.ModelViewSet):
    
    model = Cargo
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    filter_class = CargoFilter
    ordering_fields = ('descripcion',)
    search_fields = ('descripcion',)
    
    #get all
    @has_permission
    def list(self, request, *args, **kwargs):
        """
        Lista todos los cargos ordenados por id.
        \n
        Filtros posible:\n
        -descripcion=[cargo]
        """
        return viewsets.ModelViewSet.list(self, request, *args, **kwargs)
    
    #get by id
    @has_permission
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve el cargo solicitado por id.
        """
        return viewsets.ModelViewSet.retrieve(self, request, *args, **kwargs)

    #post
    @has_permission
    def create(self, request, *args, **kwargs):
        """
        Crea un nuevo cargo.
        """
        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)
    
    #put    
    @has_permission
    def update(self, request, pk=None, *args, **kwargs):
        """
        Actualiza un cargo completo.
        """
        return viewsets.ModelViewSet.update(self, request, *args, **kwargs)

    #patch
    @has_permission
    def partial_update(self, request, pk=None, *args, **kwargs):
        """
        Actualiza campos de un cargo.
        """
        return viewsets.ModelViewSet.partial_update(self, request, *args, **kwargs)

    #delete
    @has_permission
    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Elimina un cargo.
        """
        return viewsets.ModelViewSet.destroy(self, request, *args, **kwargs)
