from rest_framework import serializers
from tutorials.models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id','nombre','apellido')
