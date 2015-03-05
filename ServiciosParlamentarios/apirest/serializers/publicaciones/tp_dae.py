from rest_framework import serializers
from apirest.models.publicaciones.tp_dae import TpDae

class TpDaeSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = TpDae
#         fields = ('id','fk_publicacion_estructura','fk_bae_dae','fhapertura','fhcierre')