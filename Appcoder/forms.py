from django import forms
from django.conf import settings

class GrupoFormulario(forms.Form):
    nombregrupo = forms.CharField(max_length=40)
    actividad = forms.CharField(max_length=40)

class NotaGrupoFormulario(forms.Form):
    nombregrupo = forms.CharField(max_length=40)
    actividad = forms.CharField(max_length=40)
    nota = forms.IntegerField()

class AlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    actividad = forms.CharField(max_length=40)

class NotaAlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    actividad = forms.CharField(max_length=40)
    nota = forms.IntegerField()
