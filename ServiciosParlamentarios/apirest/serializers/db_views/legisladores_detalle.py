from rest_framework import serializers
from apirest.models.db_views.legisladores_detalle import LegisladoresDetalle

class LegisladoresDetalleSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = LegisladoresDetalle
        fields = ('id','nombre_legislador','fecha_inicio','fecha_fin','fecha_incorporacion','fecha_cese','cargo','distrito','bloque')