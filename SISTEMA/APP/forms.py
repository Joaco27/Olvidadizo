from .models import *
from django import forms
import datetime
from datetime import date
from django.core.exceptions import ValidationError 
from django.forms import widgets

class CumpleForm(forms.Form):
    fecha = forms.DateField(label="Fecha", widget=forms.DateInput(attrs= {"type":"date"}))
    descripcion = forms.CharField(label= "Cumpleañero/a", required=True)
    
    def clean_fecha(self):
        data = self.cleaned_data["fecha"]

        fecha = date.today() 
        
        data_str = data.strftime('%d/%m/%Y')
        data_nueva = datetime.datetime.strptime(data_str, '%d/%m/%Y').date()
        
        if data_nueva > fecha:
            raise ValidationError("Fecha invalida")
        return data
    
class TareaForm(forms.Form):
    fecha = forms.DateField(label="Fecha", widget=forms.DateInput(attrs= {"type":"date"}))
    descripcion = forms.CharField(label= "Tarea a realizar", required=True)
    
    def clean_fecha(self):
        data = self.cleaned_data["fecha"]

        fecha = date.today() 
        
        data_str = data.strftime('%d/%m/%Y')
        data_nueva = datetime.datetime.strptime(data_str, '%d/%m/%Y').date()
        
        if data_nueva < fecha:
            raise ValidationError("Fecha invalida")
        return data
