from django.db import models

# Create your models here.
class Tareas(models.Model):
    user = models.IntegerField()
    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=200)
    
class Cumples(models.Model): 
    user = models.IntegerField() 
    dia = models.IntegerField()
    mes = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15)
    passwords = models.CharField(max_length=15)