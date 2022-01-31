from django.urls import path
from Appcoder.views import *

urlpatterns = [
    path('curso/', curso, name="Curso"),
    path('inicio/', inicio, name="Inicio"),    
]