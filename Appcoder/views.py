from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime


# Create your views here.

#def Curso_anterior(request):
#    nombre="Coderhouse - Desarrollo APP"
#    camada="28875"
#    context=(f"El curso que está tomando es: {nombre}, y está en la camada: {camada}")
#    return HttpResponse(context)

def curso(request):
    return render(request, 'Appcoder/curso.html')

def inicio(request):
    return render(request, 'Appcoder/index.html')