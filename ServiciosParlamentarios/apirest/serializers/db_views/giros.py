from rest_framework import serializers
from apirest.models.db_views.giros import Giros

class GirosSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Giros

