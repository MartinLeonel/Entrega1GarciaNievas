from django.urls import path

from AppCoder import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('empresas', views.Empresas, name="Empresas"),
    path('jefes', views.Jefes, name="Jefes"),
    path('empleados', views.Empleados, name="Empleados"),
    path('tareas', views.Tareas, name="Tareas"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('busaaaacar/', views.buscar),
   
]

