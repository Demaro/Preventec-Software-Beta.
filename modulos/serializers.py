from django.conf import settings
from rest_framework import serializers

from modulos.models import Submodulo, Carpeta



class CarpetaSerializer(serializers.ModelSerializer):
    # If your <field_name> is declared on your serializer with the parameter required=False
    # then this validation step will not take place if the field is not included.
    
    class Meta:
        model = Carpeta
        # fields = '__all__'
        fields = ('nombre', 'porcent', 'estado', )



class SubModuloSerializer(serializers.ModelSerializer):
    # If your <field_name> is declared on your serializer with the parameter required=False
    # then this validation step will not take place if the field is not included.
    carpeta = CarpetaSerializer(many=True, read_only=True)

    class Meta:
        model = Submodulo
        # fields = '__all__'
        fields = ('nombre', 'porcent', 'estado', 'carpeta', 'tipo',)



