from rest_framework import serializers
from apirest.models.organismos.grupo_parlamentario_amistad import GrupoParlamentarioAmistad
from apirest.serializers.organismos.gpa_hist import GpaHistSerializer
from apirest.serializers.organismos.gpa_estructura import GpaEstructuraSerializer

class GrupoParlamentarioAmistadSerializer(serializers.ModelSerializer):
    
    historico = GpaHistSerializer(many=True)
    estructura = GpaEstructuraSerializer(many=True)
 
    class Meta:
        model = GrupoParlamentarioAmistad
        fields = ('id','caracter','tipo_camara', 'fecha_inicio','fecha_fin','sigla','norma_creacion','historico','estructura')
