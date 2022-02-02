from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime

from Appcoder.forms import CursoFormulario
from.models import *

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

def curso_formulario(request):

    if request.method == 'POST':
    
        miformulario = CursoFormulario(request.POST)

        #print(miformulario)

        if miformulario.is_valid:
            info = miformulario.data
            curso = Curso(nombre= info['nombre'], camada= info['camada'])
            curso.save()

    miformulario = CursoFormulario()
    
    return render(request, 'Appcoder/curso_formulario.html', {"miformulario": miformulario})

