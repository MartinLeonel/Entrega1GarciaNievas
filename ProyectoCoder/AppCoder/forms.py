from django import forms


class EmpresasFormulario(forms.Form):

    #Especificar los campos
    empresa = forms.CharField(max_length=40)
    sucursal = forms.IntegerField()


class JefesFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    area= forms.CharField(max_length=30)
    
class EmpleadoFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    
class TareasFormulario(forms.Form):
    nombre= forms.IntegerField()
    equipo= forms.IntegerField()
    