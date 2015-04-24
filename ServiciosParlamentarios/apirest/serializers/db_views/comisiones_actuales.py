from rest_framework import serializers
from apirest.models.db_views.comisiones_actuales import ComisionesActuales

class ComisionesActualesSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = ComisionesActuales
        fields = ('comision_id','nombre_comision','nombre_corto','correo','orden','caracter','tipocamara',
                  'finicio','ffin','sigla','normacreacion')