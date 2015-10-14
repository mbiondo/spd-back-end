from rest_framework import viewsets
from apirest.models.debate import Debate
from apirest.serializers.debate import DebateFullSerializer
# from apirest.filters.debate_filter import DebateFilter
from apirest.authorizers.authorizator import has_permission

class DebateViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset =  Debate.objects.all()
    serializer_class = DebateFullSerializer
#     filter_class = DebateFilter

    @has_permission    
    def list (self, request, *args, **kwargs):
        """
        Lista de todas los debates.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission
    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve un debate determinado por su id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
        