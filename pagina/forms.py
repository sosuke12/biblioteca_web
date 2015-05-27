__author__ = 'noescobar'
from django import forms


class FormularioRegistro(forms.Form):
    DNI = forms.IntegerField(required=True)
    Nombre = forms.CharField(required=True)
    Correo = forms.EmailField(required=True)


class FormularioLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
