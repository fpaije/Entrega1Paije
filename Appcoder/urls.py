from django.urls import path
from Appcoder.views import *

urlpatterns = [
    path('curso/', curso, name="AppcoderCurso"),
    path('inicio/', inicio, name="AppcoderInicio"),
    path('cursoformulario/', curso_formulario, name="AppcoderCursoFormulario"),        
]