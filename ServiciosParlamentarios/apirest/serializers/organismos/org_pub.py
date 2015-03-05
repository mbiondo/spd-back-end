from rest_framework import serializers
from apirest.models.organismos.org_pub import OrgPub

class OrgpubSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = OrgPub
#         fields = ('id','nombre','sigla','fk_org_pub','finicio','ffin','nota')