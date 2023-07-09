from django.urls import path
from .views import irIndex, filtrarPacientes, mostrarPacientes
from .views import ingresarPaciente, editarPaciente


urlpatterns = [
    path('', irIndex, name='index'),
    path('mostrar_pacientes', mostrarPacientes, name='mostrar_pacientes'),
    path('filtrar_pacientes', filtrarPacientes, name='filtrar_pacientes'),
    
    path('ingresar_paciente', ingresarPaciente, name='ingresar_paciente'),
    path('editar_paciente/<int:id>', editarPaciente, name='editar_paciente')
    
    
]
