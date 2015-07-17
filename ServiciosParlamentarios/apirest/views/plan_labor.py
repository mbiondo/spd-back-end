from rest_framework import viewsets
from apirest.models.plan_labor import PlanLabor
from apirest.serializers.plan_labor import PlanLaborSerializer
from apirest.authorizers.authorizator import has_permission

class PlanLaborViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset =  PlanLabor.objects.all()
    serializer_class = PlanLaborSerializer
#     filter_class = SancionFilter

    @has_permission        
    def list (self, request, *args, **kwargs):
        """
        Lista todas los planes de labor.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)

    @has_permission
    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve un plan de labor por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    