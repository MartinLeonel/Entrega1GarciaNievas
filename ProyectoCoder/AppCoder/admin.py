from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(Empresas)

admin.site.register(Empleados)

admin.site.register(Jefes)

admin.site.register(Tareas)
