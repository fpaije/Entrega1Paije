from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime

from .forms import *
from .models import *

def inicio(request):
    return render(request, 'Appcoder/Inicio.html')

def alumnos(request):
    if request.method == 'POST':
        miformulario = AlumnoFormulario(request.POST)
        if miformulario.is_valid:
            info = miformulario.data
            alumno = Alumno(nombre= info['nombre'], apellido= info['apellido'], email= info['email'], actividad= info['actividad'])
            alumno.save() 
    miformulario = AlumnoFormulario()
    return render(request, 'Appcoder/Alumnos.html', {"miformulario": miformulario})

def nota_alumnos(request):
    if request.method == 'POST':
        miformulario = NotaAlumnoFormulario(request.POST)
        if miformulario.is_valid:
            info = miformulario.data
            nota_alumno = NotaAlumno(nombre= info['nombre'], apellido= info['apellido'], actividad= info['actividad'], nota= info['nota'])
            nota_alumno.save() 
    miformulario = NotaAlumnoFormulario()
    return render(request, 'Appcoder/NotaAlumnos.html', {"miformulario": miformulario})

def grupos(request):
    if request.method == 'POST':
        miformulario = GrupoFormulario(request.POST)
        if miformulario.is_valid:
            info = miformulario.data
            grupos = Grupo(nombregrupo= info['nombregrupo'], actividad= info['actividad'])
            grupos.save() 
    miformulario = GrupoFormulario()
    return render(request, 'Appcoder/Grupos.html', {"miformulario": miformulario})

def notagrupos(request):
    if request.method == 'POST':
        miformulario = NotaGrupoFormulario(request.POST)
        if miformulario.is_valid:
            info = miformulario.data
            nota = NotaGrupo(nombregrupo= info['nombregrupo'], actividad= info['actividad'], nota= info['nota'])
            nota.save() 
    miformulario = NotaGrupoFormulario()
    return render(request, 'Appcoder/nota_template.html', {"miformulario": miformulario})

def busquedaGrupo (request):
    return render(request, 'Appcoder/busquedaGrupo.html')

def buscarGrupo(request):
    if request.GET['grupo']:
        nombregrupo=request.GET['grupo']
        actividades = NotaGrupo.objects.filter(nombregrupo__icontains=nombregrupo)
        notas = NotaGrupo.objects.filter(nombregrupo__icontains=nombregrupo)
        return render(request, 'Appcoder/resultadoBusqueda.html', {'actividad':actividades, 'nombregrupo':nombregrupo, 'nota':notas})
    else:
        respuesta = 'no enviaste datos'

    #return HttpResponse(respuesta)   
    return render(request, 'Appcoder/Inicio.html', {'respuesta':respuesta})

