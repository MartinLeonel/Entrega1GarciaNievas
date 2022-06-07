from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Empresas, Empleados, Jefes, Tareas
from AppCoder.forms import EmpresasFormulario, JefesFormulario, EmpleadoFormulario, TareasFormulario

# Create your views here.

def Empresas(request):

      if request.method == 'POST':

            miFormulario = EmpresasFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  empresa = Empresas (nombre=informacion['nombre'], sucursal=informacion['sucursal'],)

                  empresa.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= EmpresasFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/empleados.html", {"miFormulario":miFormulario})
      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")



def Tareas(request):

      if request.method == 'POST':

            miFormulario = TareasFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  empresa = Empresas (nombre=informacion['empresa'], equipo=informacion['equipo']) 

                  empresa.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= TareasFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/empresas.html", {"miFormulario":miFormulario})




def Jefes(request):

      if request.method == 'POST':

            miFormulario = JefesFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  jefes = Jefes (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  jefes.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= JefesFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/jefes.html", {"miFormulario":miFormulario})


def Empleados(request):

      if request.method == 'POST':

            miFormulario = EmpleadoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  empleado = Empleados (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'])

                  empleado.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= EmpleadoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/empleados.html", {"miFormulario":miFormulario})



def buscar(request):

      if  request.GET["Tareas"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            equipo = request.GET['equipo'] 
            nombre = Tareas.objects.filter(equipo__icontains=equipo)

            return render(request, "AppCoder/inicio.html", {"nombre":nombre, "equipo":equipo})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

