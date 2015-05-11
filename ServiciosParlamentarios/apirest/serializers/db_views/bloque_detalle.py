from rest_framework import serializers
from apirest.models.db_views.bloque_detalle import BloqueDetalle

class BloqueDetalleSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BloqueDetalle
        fields = ('nombre_legislador','cargo','jerarquia','estado','fecha_desde',
                  'fecha_hasta','cargo_legislador','partido','fecha_inicio_legislador','fecha_fin_legislador')
        