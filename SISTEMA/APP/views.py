from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'paginas/index.html')

def cumpleMes(request, mes):
    cumples = [
        {'dia': 1,'mes':1,'descripcion':"Juan"},
        { 'dia': 2,'mes':2,'descripcion':"Maria"},
        { 'dia': 3,'mes':3,'descripcion':"Ana"},
        {'dia': 1,'mes':1,'descripcion':"Joaquin"},
        { 'dia': 2,'mes':2,'descripcion':"Fernando"},
        { 'dia': 3,'mes':3,'descripcion':"Oscar"},
    ]
    context=[]
    for c in cumples:
        if c['mes'] == mes:
            context.append(c)
    return render(request, 'paginas/cumplePorMes.html', {'context':context})
         

def agregarCumple(request):
    if request.method == 'POST':
        cumple_form = CumpleForm(request.POST)
        if cumple_form.is_valid():

            messages.add_message(request, messages.SUCCESS, 'Consulta enviada con exito', extra_tags="tag1")

            return redirect("index")
    else:
        cumple_form = CumpleForm()
        
    context = {
        'form': cumple_form,
    }
    return render(request, 'paginas/agregarCumple.html', context)


def agregarTarea(request):
    if request.method == 'POST':
        tarea_form = TareaForm(request.POST)
        if tarea_form.is_valid():

            messages.add_message(request, messages.SUCCESS, 'Consulta enviada con exito', extra_tags="tag1")

            return redirect("index")
    else:
        tarea_form = TareaForm()
        
    context = {
        'form': tarea_form,
    }
    return render(request, 'paginas/agregarTarea.html',context)

    

def verCumples(request):
    #context=Cumples.objects.all()
    context = [
        {
            'dia': 1,
            'mes':1,
            'descripcion':"Juan"
        },
        {
            'dia': 2,
            'mes':2,
            'descripcion':"Maria"
        },
        {
            'dia': 3,
            'mes':3,
            'descripcion':"Ana"
        },
    ]
    return render(request, 'paginas/verCumples.html', {'context':context})

def verTareas(request):
    #context=Tareas.objects.all()
    context = [
        {
            'fecha': '4/5/2023',
            'descripcion':"Realizar web python django"
        },
        {
            'fecha': '4/5/2023',
            'descripcion':"Realizar web python django"
        },
        {
            'fecha': '4/5/2023',
            'descripcion':"Realizar web python django"
        },
    ]
    return render(request, 'paginas/verTareas.html', {'context':context})

def LogIn(request):
    return render(request, 'paginas/LogIn.html')