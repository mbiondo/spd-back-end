from rest_framework import serializers
from apirest.models.db_views.bloque_detalle import BloqueDetalle

class BloqueDetalleSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BloqueDetalle
        fields = ('nombre_legislador','cargo','jerarquia','estado','fdesde',
                  'fhasta','cargo_legislador','partido','finicio_legislador','ffin_legislador')
        