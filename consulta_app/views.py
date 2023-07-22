from django.shortcuts import render, redirect
from .forms import ConsultaForm
from gestion_pacientes.models import Paciente
from django.contrib import messages
from .models import Consulta

# Create your views here.
def nuevaConsulta(request, id):
    paciente = Paciente.objects.get(pk=id)
    
    if request.method == 'POST':
        consulta_form = ConsultaForm(request.POST)
        if consulta_form.is_valid():
            consulta = consulta_form.save(commit=False)
            consulta.id_paciente = paciente
            consulta.save()
            messages.success(request, 'Consulta ingresada!')
            return redirect('mostrar_pacientes')
            
            
    else:
        consulta_form = ConsultaForm()
    
    return render(request, 'consulta/nueva_consulta.html', {'consulta_form': consulta_form})


def historialConsulta(request, id):
    consultas = Consulta.objects.filter(id_paciente=id).order_by('-fecha_consulta')
    
    return render(request, 'consulta/historial.html', {'consultas': consultas, 'id': id})


def verConsulta(request, id):
    consulta = Consulta.objects.get(pk=id)
    consulta_form = ConsultaForm(instance=consulta)
    
    return render(request, 'consulta/ver_consulta.html', {'consulta_form': consulta_form, 'consulta': consulta})