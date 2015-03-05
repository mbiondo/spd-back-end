from rest_framework import serializers
from apirest.models.individuos.persona_fisica_hist import PersonaFisicaHist

class PersonaFisicaHistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PersonaFisicaHist
#         fields = ('id','nombre','apellido','genero','apellidocasada','email','profesion','titulo','tratamiento','direccion','localidad',
#                   'estadocivil','telefono','conyuge','fdesde','fhasta')