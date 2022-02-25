from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=70,blank=False, default='')
    apellido=models.CharField(max_length=70,blank=False, default='')
