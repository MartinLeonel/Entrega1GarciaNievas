from django.db import models

# Create your models here.
class Empresas(models.Model):

    nombre=models.CharField(max_length=40)
    sucursal = models.IntegerField()


class Empleados(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Jefes(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    area= models.CharField(max_length=30)

class Tareas(models.Model):
    nombre= models.CharField(max_length=30)
    equipo = models.CharField(max_length=30)  
    
