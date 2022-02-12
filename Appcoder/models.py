from django.db import models
from django.conf import settings
from ProyectoCoder.settings import *

# Create your models here.

class Grupo(models.Model):
    nombregrupo = models.CharField(max_length=40)
    actividad = models.CharField(max_length=40)

class NotaGrupo(models.Model):
    nombregrupo = models.CharField(max_length=40)
    actividad = models.CharField(max_length=40)
    nota = models.IntegerField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    actividad = models.CharField(max_length=40)

class NotaAlumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    actividad = models.CharField(max_length=40)
    nota = models.IntegerField()
