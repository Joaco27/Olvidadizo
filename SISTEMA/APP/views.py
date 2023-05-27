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
        form = CumpleForm(request.POST)
        u = Users.objects.get(username='joaco27')
        if form.is_valid():
            
            cumpleaños_nuevo = Cumples(
                user = u,
                fecha = form.cleaned_data['fecha'],
                descripcion = form.cleaned_data['descripcion'],
            )

            cumpleaños_nuevo.save()
            messages.add_message(request, messages.SUCCESS, 'Consulta enviada con exito', extra_tags="tag1")

            return redirect("index")
    else:
        form = CumpleForm()
        
    context = {
        'form': form,
    }
    return render(request, 'paginas/agregarCumple.html', context)


def agregarTarea(request):
    if request.method == 'POST':
        u = Users.objects.get(username='joaco27')
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea_nueva = Tareas(
                user = u,
                fecha = form.cleaned_data['fecha'],
                descripcion = form.cleaned_data['descripcion'],
            )

            tarea_nueva.save()
            messages.add_message(request, messages.SUCCESS, 'Consulta enviada con exito', extra_tags="tag1")

            return redirect("index")
    else:
        form = TareaForm()
        
    context = {
        'form': form,
    }
    return render(request, 'paginas/agregarTarea.html',context)

    

def verCumples(request):
    context=Cumples.objects.all()

    return render(request, 'paginas/verCumples.html', {'context':context})

def verTareas(request):
    context=Tareas.objects.all()
    
    return render(request, 'paginas/verTareas.html', {'context':context})

def LogIn(request):
    return render(request, 'paginas/LogIn.html')