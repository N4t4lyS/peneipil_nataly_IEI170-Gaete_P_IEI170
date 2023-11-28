from django import forms
from .models import Reserva
from datetime import date
from django.core import validators 

#Todos los campos son obligatorios, excepto la observación, la cantidad de personas debe 
#estar entre 1 y 15, validación de correo electrónico, el nombre de la persona no puede 
#superar los 80 caracteres.

class formReserva(forms.ModelForm):
    class Meta:
        model=Reserva
        fields='__all__'
        widgets = {
            'fechaReserva': forms.DateInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy', 'placeholder': 'DD-MM-YYYY'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),

        }

    def clean_cantidadPersonas(self):
        cantidad_personas = self.cleaned_data['cantidadPersonas']
        if cantidad_personas < 1 or cantidad_personas > 15:
            raise forms.ValidationError('La cantidad de personas debe estar entre 1 y 15.')
        return cantidad_personas

    def clean_email(self):
        inputemail = self.cleaned_data['email']
        if inputemail.find('@') == -1:
            raise forms.ValidationError("El correo debe contener un @")
        return inputemail

    def clean_nombre(self):
        nombre=self.cleaned_data['nombre']
        if len(nombre)>80:
            raise forms.ValidationError("El nombre supera los 80 caracteres")
        return nombre

