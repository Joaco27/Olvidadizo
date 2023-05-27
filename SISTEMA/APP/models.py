from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=15)
    passwords = models.CharField(max_length=15)

class Tareas(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=200)
    
class Cumples(models.Model): 
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=200)
    
