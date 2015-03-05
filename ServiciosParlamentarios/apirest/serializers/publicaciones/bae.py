from rest_framework import serializers
from apirest.models.publicaciones.bae import Bae

class BaeSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Bae
#         fields = ('id','fk_publicacion_estructura','numero','fhapertura','fhcierre','fk_camara_reunion','tipo')
