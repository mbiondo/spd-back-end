from rest_framework import serializers
from apirest.models.db_views.giros import Giros

class GirosSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Giros
        fields = ('id','proyecto','comision_id','codigo_exp','comision_nombre','comision_nombre_corto','order_giro')
