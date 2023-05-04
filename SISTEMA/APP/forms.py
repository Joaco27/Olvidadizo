from .models import *
from django import forms
import datetime
from datetime import date
from django.core.exceptions import ValidationError 

class CumpleForm(forms.Form):
    dia = forms.IntegerField(label= "Dia", required=True)
    mes = forms.IntegerField(label= "Mes", required=True)
    descripcion = forms.CharField(label= "Cumpleañero/a", required=True)
    
    def clean_dia(self):
        data = self.cleaned_data["dia"]
        if data < 1 or data > 31:
            raise ValidationError("Dia invalido")
        return data
    
    def clean_mes(self):
        data = self.cleaned_data["mes"]
        if data < 1 or data > 12:
            raise ValidationError("Mes invalido")
        return data
    
class TareaForm(forms.Form):
    #fecha = forms.DateField(label= "Fecha", required=True, widget=forms.DateInput())
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