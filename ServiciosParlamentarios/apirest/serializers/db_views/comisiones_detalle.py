from rest_framework import serializers
from apirest.models.db_views.comision_detalle import ComisionesDetalle

class ComisionesDetalleSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = ComisionesDetalle
        fields = ('nombre_legislador','cargo','estado','fecha_desde','fecha_hasta')