from rest_framework import serializers
from apirest.models.db_views.legisladores_detalle import LegisladoresDetalle

class LegisladoresDetalleSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = LegisladoresDetalle
        fields = ('nombre_legislador','finicio','ffin','fincorporacion','fcese','cargo','distrito','bloque')