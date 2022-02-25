from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from tutorials.models import Persona
from tutorials.serializers import PersonaSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def persona_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
     if request.method == 'GET':
        personas = Persona.objects.all()
        
        nombre = request.GET.get('nombre', None)
        if nombre is not None:
            personas = personas.filter(nombre__icontains=nombre)
        
        persona_serializer = PersonaSerializer(personas, many=True)
        return JsonResponse(persona_serializer.data, safe=False)


@api_view(['GET','POST','DELETE'])
def persona_save(request):
    if request.method == 'POST':
        persona_data = JSONParser().parse(request)
        persona_serializer = PersonaSerializer(data=persona_data)
        if persona_serializer.is_valid():
            persona_serializer.save()
            return JsonResponse(persona_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(persona_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def search_persona(request,pk):
    persona = Persona.objects.get(pk=pk)
    if request.method == 'GET':
        persona_serializer = PersonaSerializer(persona)
        return JsonResponse(persona_serializer.data)
    elif request.method == 'DELETE':
        persona.delete()
        return JsonResponse({'message':'Eliminado'}, status=status.HTTP_204_NO_CONTENT)
    








# Create your views here.
