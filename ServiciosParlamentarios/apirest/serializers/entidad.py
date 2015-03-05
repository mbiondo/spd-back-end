from rest_framework import serializers
from apirest.models.entidad import Entidad
from apirest.serializers.organismos.camara import CamaraSerializer
from apirest.utils.constants import Constants
from apirest.serializers.organismos.bloques.bloque import BloqueSerializer
from apirest.serializers.individuos.persona_fisica import PersonaFisicaSerializer
from apirest.serializers.organismos.comisiones.comision import ComisionChildSerializer
from apirest.serializers.organismos.org_pub import OrgpubSerializer

class EntidadSerializer(serializers.ModelSerializer):  
    
    #read-only field
    entidad = serializers.SerializerMethodField('get_hijo')   
   
    def get_hijo(self, Entidad):
        if hasattr(Entidad, Constants().CAMARA):
            return CamaraSerializer(Entidad.camara,required=False).data
        elif hasattr(Entidad, Constants().BLOQUE): 
            return BloqueSerializer(Entidad.bloque, required=False).data
        elif hasattr(Entidad, 'personafisica'):
            return PersonaFisicaSerializer(Entidad.personafisica, required=False).data
        elif hasattr(Entidad, Constants().COMISION):
            return ComisionChildSerializer(Entidad.comision, required=False).data
        elif hasattr(Entidad, Constants().ORG_PUB):
            return OrgpubSerializer(Entidad.orgpub, required=False).data
        else:
            return EntidadSerializer(required=False).data
   
    class Meta:
        model = Entidad
        fields = ('id','selector','descripcion', 'entidad')