from django.urls import path
from Appcoder.views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('alumnos/', alumnos, name="Alumnos"),
    path('notaalumnos/', nota_alumnos, name="NotaAlumnos"),
    path('grupos/', grupos, name="Grupos"),        
    path('notagrupos/', notagrupos, name="nota_template"),
    path('busquedaGrupo/', busquedaGrupo, name="busquedaGrupo"),
    path('buscarGrupo/', buscarGrupo),    
]