from rest_framework import serializers
from apirest.models.organismos.gpa_hist import GpaHist

class GpaHistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GpaHist
